import ast
import contextlib
import os
from io import StringIO
import stat
import json
from csv import DictReader
from pathlib import Path
from argparse import ArgumentParser
from subprocess import check_output, CalledProcessError, PIPE, TimeoutExpired, Popen
from urllib.request import urlretrieve, urlopen
from functools import lru_cache, cache
from zipfile import ZipFile
from os.path import exists
from shutil import copyfileobj
from tqdm import tqdm

parser = ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--binary', required=True)
args = parser.parse_args()

url = "https://github.com/duckdb/duckdb/releases/download/{version}/duckdb_cli-linux-amd64.zip"


@cache
def get_versions():
    versions = sorted(
        [
            version["tag_name"]
            for version in json.load(
                urlopen("https://api.github.com/repos/duckdb/duckdb/releases")
            )
        ]
    )
    # can't find working binaries for versions older than v0.1.9
    return versions[versions.index("v0.1.9") :]


@lru_cache()
def get_duck(version: str) -> str:
    dest = Path(f"duckdb-{version}")
    if not dest.exists():
        filename, _ = urlretrieve(url.format(version=version))

        with ZipFile(filename) as zipfile, dest.open("wb") as fh:
            copyfileobj(zipfile.open("duckdb"), fh)

        os.chmod(dest, dest.stat().st_mode | stat.S_IEXEC)

    return str(dest.resolve())


def find_added_version(example):
    versions = get_versions()
    oldest_version = versions[0]

    for version in versions:
        with contextlib.suppress(CalledProcessError):
            path = get_duck(version)
            get_raw_result(path, example)
            return (
                f"{oldest_version} or prior"
                if version == oldest_version
                else version
            )
    return "indeterminate, example passed in no versions"


def get_raw_result(binary: str, example: str) -> str:
    proc = Popen(
        [
            binary,
            "-csv",
            # '-cmd',
            # 'SELECT setseed(0.42); ',
            # '-cmd',
            # 'LOAD icu;',
            "-batch",
        ],
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        stdin=PIPE,
    )
    if "enum" in example.lower():
        proc.stdin.write(
            "CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy', 'anxious');\n"
        )

    proc.stdin.write(f'SELECT {example.strip(";")} AS result;\n')
    proc.stdin.close()
    out = proc.stdout.read()
    if err := proc.stderr.read():
        raise CalledProcessError(
            output=out, stderr=err, cmd="", returncode=proc.returncode
        )

    rows = list(DictReader(StringIO(out)))
    if not rows:
        return None

    result = rows[0]["result"]
    try:
        if result in ['true', 'false']:
            return result == 'true'
        else:
            return ast.literal_eval(result)
    except (SyntaxError, ValueError):
        return result


def get_result(example: str) -> str:
    if example == 'current_date()':
        return '2023-07-23'
    elif example == 'get_current_time()':
        return '14:04:22.524'
    elif example == 'get_current_timestamp()':
        return '2023-07-23 14:04:22.538+00'
    elif example == 'version()':
        return 'v0.8.1'

    try:
        return get_raw_result(args.binary, example)
    except CalledProcessError as e:
        print(e.stderr)
        return None


def main():
    functions = []
    source = Path(args.source)
    assert source.exists()

    for version in tqdm(get_versions(), desc='Loading DuckDB versions'):
        get_duck(version)

    with open('docs/functions.json') as fh:
        existing_functions = {
            function['name']: function.get('added_in_version')
            for function in json.load(fh)
            if 'version' in function
        }

    existing_functions.clear()  # TODO: remove me

    for file in source.glob('src/core_functions/**/*.json'):
        category = file.parent.stem
        with file.open() as fh:
            functions += [
                {
                    **function,
                    'name': function['name'].replace('__postfix', ''),
                    'parameters': (
                        [x.strip() for x in function['parameters'].split(',')]
                        if function.get('parameters')
                        else []
                    ),
                    'category': category,
                    'added_in_version': existing_functions.get(
                        function['name'],
                        find_added_version(function['example']),
                    )
                    if 'scalar' in function['type']
                    else None,
                    'result': get_result(function['example'])
                    if function.get('example') and 'scalar' in function['type']
                    else None,
                }
                for function in json.load(fh)
            ]

    functions = sorted(functions, key=lambda fn: fn['name'])

    with open('docs/functions.json', 'w') as fh:
        json.dump(functions, fh, indent=2)


if __name__ == '__main__':
    main()

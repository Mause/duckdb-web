import sys
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
from functools import cache
from zipfile import ZipFile
from os.path import exists
from shutil import copyfileobj
from tqdm import tqdm
from typing import Set

parser = ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--binary', required=True)
args = parser.parse_args()

match sys.platform:
    case 'linux':
        platform = 'linux-amd64'
    case 'darwin':
        platform = 'osx-universal'
    case 'win32':
        platform = 'windows-amd64'
url = f"https://github.com/duckdb/duckdb/releases/download/{{version}}/duckdb_cli-{platform}.zip"


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
    # we don't provide docs for versions older than this
    return versions[versions.index("v0.4.0") :]


@cache
def get_duck(version: str) -> str:
    dest = Path(f"duckdb-{version}")
    if not dest.exists():
        filename, _ = urlretrieve(url.format(version=version))

        with ZipFile(filename) as zipfile, dest.open("wb") as fh:
            copyfileobj(zipfile.open("duckdb"), fh)

        os.chmod(dest, dest.stat().st_mode | stat.S_IEXEC)

    return str(dest.resolve())


def find_added_version(function: dict) -> str:
    versions = get_versions()
    oldest_version = versions[0]

    for version in versions:
        with contextlib.suppress(CalledProcessError, BrokenPipeError):
            if function['name'] in get_functions(version):
                return version


@cache
def get_functions(version: str) -> Set[str]:
    return set(
        get_raw_result(
            get_duck(version), 'function_name as result from duckdb_functions()'
        )
    )


def load_data(out: str):
    dd = json._default_decoder
    end = 0
    rows = []
    while out[end:]:
        obj, end = dd.raw_decode(out, end)
        end += 1
        rows.append(obj)
    return rows


def get_raw_result(binary: str, example: str) -> str:
    extra = []
    if "enum" in example.lower():
        extra.extend(
            ['-c', "CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy', 'anxious');"]
        )

    out = check_output(
        [
            binary,
            '-json',
            '-c',
            'SELECT setseed(0.42); ',
            '-c',
            'LOAD icu;',
            *extra,
            '-c',
            f'SELECT {example.strip(";")} AS result',
        ],
        stderr=PIPE,
        text=True,
    )
    rows = load_data(out)[-1]
    return [row['result'] for row in rows]


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
        return get_raw_result(args.binary, example)[0]
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
                        find_added_version(function),
                    ),
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

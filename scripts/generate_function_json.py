import json
from pathlib import Path
from argparse import ArgumentParser
from subprocess import check_output, CalledProcessError, PIPE

parser = ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--binary', required=True)
args = parser.parse_args()

ducks = sorted(
    [
        (filename.name.split('-')[1], filename)
        for filename in Path('~/Downloads').expanduser().glob('duckdb-*')
    ]
)


def find_added_version(example):
    for version, path in ducks:
        #        get_raw_result(path, 'count(*) result from duckdb_functions()')
        try:
            get_raw_result(path, example)
            return version
        except CalledProcessError:
            pass
    return 'unknown'


def get_raw_result(binary: str, example: str) -> str:
    out = check_output(
        [
            binary,
            '-json',
            '-c',
            'SELECT setseed(0.42); ',
            '-c',
            'LOAD icu;',
            '-c',
            f'SELECT {example.strip(";")} AS result',
        ],
        stderr=PIPE,
    )
    rows = json.loads(out.splitlines()[-1])
    return rows[0]['result']


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
        print(example.strip(), e.stderr.decode())
        return None


def main():
    functions = []
    source = Path(args.source)
    assert source.exists()
    current_version = get_raw_result(args.binary, 'version()')[1:]

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
                    'result': get_result(function['example'])
                    if function.get('example')
                    else None,
                    'added_in_version': existing_functions.get(
                        function['name'],
                        find_added_version(function['example']),  # current_version
                    ),
                }
                for function in json.load(fh)
            ]

    functions = sorted(functions, key=lambda fn: fn['name'])

    with open('docs/functions.json', 'w') as fh:
        json.dump(functions, fh, indent=2)


if __name__ == '__main__':
    main()

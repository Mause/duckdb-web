import duckdb
from marko.ext.gfm.elements import Table, TableRow, TableCell
from marko.inline import RawText, CodeSpan
from marko.block import HTMLBlock
from marko.md_renderer import MarkdownRenderer
import re
import argparse
import marko
from pathlib import Path
import json
from rich import print
from ripgrepy import Ripgrepy
from markdown_table import XGFM

regex = r"<!-- function table: (.*?) -->"
docs_root = Path(__file__).parent.parent / "docs" / "sql" / "functions"

parser = argparse.ArgumentParser()
parser.add_argument('duckdb_source')
args = parser.parse_args()


def extract_text(parse_node):
    if not hasattr(parse_node, 'children'):
        return ''
    elif isinstance(parse_node.children, str):
        return parse_node.children.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    return ' '.join(extract_text(child) for child in parse_node.children)


def load_functions():
    for filename in (Path(args.duckdb_source) / 'src' / 'core_functions').glob('**/functions.json'):
        with filename.open() as fh:
            yield from json.load(fh)




def process_file(functions, filename: str):
    with open(filename) as fh:
        data = fh.read()

    markdown = marko.Markdown(extensions=[XGFM], renderer=MarkdownRenderer)
    ast = markdown.parse(data)

    for idx, child in enumerate(ast.children):
        if isinstance(child, Table):
            comment = ast.children[idx-1]
            print('found table', type(comment), end=' ')

            if isinstance(comment, HTMLBlock):
                predicate = re.match(regex, extract_text(comment)).group(1)
                print(f'found dest, {predicate=}')
                functions_for_table = [function for function in functions if eval(
                    predicate, {}, dict(function))]
                process_table(child, functions_for_table)
            else:
                print('no comment found')

    # # all functions should be bucketed under docs/sql/functions somewhere
    ret = markdown.render(ast)
    with open(filename, 'w') as fh:
        fh.write(ret)


def make(txt: str):
    node = TableCell.__new__(TableCell)
    node.children = [RawText(txt)]
    return node


def make_CodeSpan(txt: str):
    inst = CodeSpan.__new__(CodeSpan)
    inst.children = txt
    return inst


def process_table(child, functions_for_table):
    for f in functions_for_table:
        args = ', '.join(f'*`{arg}`*' for arg in f['parameters'].split(','))

        name = f"`{f['name']}(`{args}`)`"

        result = duckdb.sql(
            f"select [4, 5, 6] as l, {f['example']} as result").fetchone()[1]

        child.children.append(TableRow([
            make(name),
            make(f['description']),
            make_CodeSpan(f['example']),
            make_CodeSpan(str(result))
        ]))



def main():
    run = Ripgrepy(regex, str(docs_root)).only_matching().replace(
        '$1').json().run()

    functions = list(load_functions())

    for match in run.as_dict:
        process_file(functions, match['data']['path']['text'])



if __name__ == '__main__':
    main()

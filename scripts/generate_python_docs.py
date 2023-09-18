from sphinx.locale import __
from os.path import join, dirname, splitext, normpath
from lxml.html import fromstring, tostring, parse
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.writers.html5 import HTML5Translator
from docutils.nodes import SkipChildren
from importlib.metadata import version


FRONTMATTER = """\
---
# this file is GENERATED, regenerate it with scripts/generate_python_docs.py
layout: docu
title: {title}
---
"""


class JekyllBuilder(StandaloneHTMLBuilder):
    name = "jekyll"
    format = "markdown"
    epilog = __("The jekyll files are in %(outdir)s.")

    allow_parallel = True

    def copy_static_files(self) -> None:
        pass


def setup(app):
    app.add_builder(JekyllBuilder)


def post_process(title: str, filename: Path):
    with filename.open() as fh:
        html = fh.read()

    (doc,) = fromstring(html).xpath(".//div[@class='documentwrapper']")

    filename = splitext(filename)[0] + ".md"

    contents = tostring(doc, pretty_print=True).decode()
    contents = '\n'.join(line.lstrip() for line in contents.splitlines())

    with open(filename, "w") as fh:
        fh.write(FRONTMATTER.format(title=title) + contents)


def unlink_all(destdir: Path, pattern: str) -> None:
    for feh in destdir.glob(pattern):
        feh.unlink()


def main():
    print(
        'generating against duckdb version',
        version('duckdb'),
        'and pandas version',
        version('pandas'),
    )

    destdir = (Path(__file__).parent / "../docs/api/python/reference/").resolve()
    app = Sphinx(
        srcdir=str(destdir / "templates"),
        confdir=None,
        outdir=str(destdir),
        doctreedir="/tmp/",
        confoverrides={
            "project": "duckdb",
            "extensions": [
                "sphinx.ext.intersphinx",
                "sphinx.ext.autodoc",
                "generate_python_docs",
            ],
            "html_theme": "basic",
            "html_show_sourcelink": False,
            "html_copy_source": False,
            "html_show_sphinx": False,
            "html_use_index": False,
            "intersphinx_mapping": {
                "pandas": (
                    "https://pandas.pydata.org/pandas-docs/version/1.5.1/",
                    None,
                ),
                "pyarrow": ("https://arrow.apache.org/docs/9.0/", None),
                "fsspec": ("https://filesystem-spec.readthedocs.io/en/latest/", None),
            },
        },
        buildername="jekyll",
    )

    app.build(True)

    unlink_all(destdir, '**/*.md')

    for source in destdir.glob('**/*.html'):
        if source.stem in ('genindex', 'search', 'py-modindex'):
            continue
        title, = parse(source.open('rb')).xpath('.//title/text()')
        title = title.split(' — ', 1)[0]

        # assert title != '<no title>', f'{source} has no title'

        post_process(title, source)

        print(title,source)

    for ext in ('html', 'txt'):
        unlink_all(destdir, f"**/*.{ext}")

if __name__ == "__main__":
    main()

from marko.ext.gfm import GFM
from marko.md_renderer import MarkdownRenderer


class Mixin():
    def render_row(self, row, widths):
        return '| {} |'.format(' | '.join((cell if isinstance(cell, str) else self.render(cell)).ljust(widths[idx]) for idx, cell in enumerate(row)))

    def render_table(self, table):
        header, *rows = table.children

        rows = [
            [
                self.render(cell)
                for cell in row.children
            ]
            for row in rows
        ]
        widths = [max(len(row[i]) for row in rows)
                  for i in range(len(rows[0]))]

        sep = '|:{}|'.format(
            '|:'.join(
                '-' * (widths[idx] + 1) for idx in range(len(header.children))))

        parts = [
            self.render_row(header.children, widths),
            sep,
            *[
                self.render_row(row, widths)
                for row in rows
            ]
        ]
        return '\n'.join(parts) + '\n\n'

    def render_html_block(self, block):
        with MarkdownRenderer() as ren:
            return ren.render_html_block(block).strip() + '\n'


class XGFM(GFM):
    renderer_mixins = [Mixin]

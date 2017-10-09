import pkg_resources

from docutils import nodes
from docutils.parsers.rst import Directive, directives


class PiximgNode(nodes.General, nodes.Element):
    pass


class PiximgDirective(Directive):
    required_arguments = 1
    option_spec = {
        'size': directives.unchanged,
        'border': directives.unchanged,
    }

    def run(self):
        return [PiximgNode(
            embed_id=self.arguments[0],
            embed_size=self.options.get('size', 'large'),
            embed_border=self.options.get('border', 'off'),
        )]


def visit_pixiv(self, node):
    self.body.append(self.starttag(
        node, 'div',
        **{
            'class': 'pixiv-embed',
            'data-id': node['embed_id'],
            'data-size': node['embed_size'],
            'data-border': node['embed_border'],
        }
    ))
    self.body.append('</div>')
    raise nodes.SkipNode


def embed_js(app):
    app.add_javascript('https://source.pixiv.net/source/embed.js')


def setup(app):
    app.add_node(PiximgNode, html=(visit_pixiv, None))
    app.add_directive('piximg', PiximgDirective)
    app.connect('builder-inited', embed_js)

    return {
        'version': pkg_resources.get_distribution('piximg').version,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

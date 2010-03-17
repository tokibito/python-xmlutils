from xml.sax.saxutils import XMLGenerator

from xmlutils.renderer.base import BaseRenderer

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

# SimplerXMLGenerator class from django.utils.xmlutils
class SimplerXMLGenerator(XMLGenerator):
    def addQuickElement(self, name, contents=None, attrs=None, unichar=False):
        "Convenience method for adding an element with no children"
        if attrs is None: attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            if unichar:
                self.unicode_characters(contents)
            else:
                self.characters(contents)
        self.endElement(name)

    def unicode_characters(self, contents):
        self._write(str(''.join(map(lambda c: '&#%d;' % ord(c), contents))))
# --

class XMLRenderer(BaseRenderer):
    def _render_node(self, handler, node, indent=None, depth=0, unichar=False):
        if node.has_content():
            if indent:
                handler._write(' ' * depth)
            handler.addQuickElement(node.name, node.content, unichar=unichar)
            if indent:
                handler._write('\n')
        else:
            if indent:
                handler._write(' ' * depth)
            handler.startElement(node.name, node.attrs)
            if indent:
                handler._write('\n')
            for child_node in node.childs:
                n_depth = depth
                if not indent is None:
                    n_depth += indent
                self._render_node(handler, child_node, indent, n_depth, unichar)
            if indent:
                handler._write(' ' * depth)
            handler.endElement(node.name)
            if indent:
                handler._write('\n')

    def render(self, node, out=None, encoding='utf-8', indent=None, unichar=False):
        stream = StringIO()
        handler = SimplerXMLGenerator(out=stream, encoding=encoding)
        handler.startDocument()
        self._render_node(handler, node, indent, unichar=unichar)
        if not out is None:
            out.write(stream.getvalue())
        else:
            return stream.getvalue()

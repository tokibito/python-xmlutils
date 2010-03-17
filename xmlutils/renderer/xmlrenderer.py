from xml.sax.saxutils import XMLGenerator

from xmlutils.renderer.base import BaseRenderer

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

# SimplerXMLGenerator class from django.utils.xmlutils
class SimplerXMLGenerator(XMLGenerator):
    def addQuickElement(self, name, contents=None, attrs=None):
        "Convenience method for adding an element with no children"
        if attrs is None: attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            self.characters(contents)
        self.endElement(name)
# --

class XMLRenderer(BaseRenderer):
    def _render_node(self, handler, node, indent=None, depth=0):
        if node.has_content():
            if indent:
                handler._write(' ' * depth)
            handler.addQuickElement(node.name, node.content)
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
                self._render_node(handler, child_node, indent, n_depth)
            if indent:
                handler._write(' ' * depth)
            handler.endElement(node.name)
            if indent:
                handler._write('\n')

    def render(self, node, out=None, encoding='utf-8', indent=None):
        stream = StringIO()
        handler = SimplerXMLGenerator(out=stream, encoding=encoding)
        handler.startDocument()
        self._render_node(handler, node, indent)
        if not out is None:
            out.write(stream.getvalue())
        else:
            return stream.getvalue()

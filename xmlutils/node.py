from types import DictType, ListType

class Node(object):
    def __init__(self, name, content=None, attrs=None):
        self.name = name
        if attrs is None:
            attrs = {}
        self.attrs = attrs
        self.childs = []
        self.content = content

    def has_content(self):
        return not self.content is None

    def add_child(self, node):
        self.childs.append(node)

    def add_childs(self, nodes):
        self.childs.extend(nodes)

    def __repr__(self):
        if self.has_content():
            content = repr(self.content)
        else:
            content = ', '.join([repr(node) for node in self.childs])
        return '<%s %s: %s>' % (self.__class__.__name__, self.name, content)

def dict_to_node(dic, parent=None, is_root=True):
    node_list = []
    for k, v in dic.iteritems():
        node = Node(k)
        if k == '_attrs':
            parent.attrs = v
            continue
        elif type(v) == DictType:
            node.add_childs(dict_to_node(v, parent=node, is_root=False))
        elif type(v) == ListType:
            node.add_childs(reduce(lambda x,y:x+y, map(lambda m: dict_to_node(m, parent=node, is_root=False), v)))
        else:
            node.content = v
        node_list.append(node)
    if is_root:
        return node_list[0]
    return node_list

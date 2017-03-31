from model.HdlElement import HdlElement


class Entity(HdlElement):
    def __init__(self, name):
        self.name = name
        self.generics = []
        self.ports = []

    def __str__(self):
        return "<Entity name={0}>".format(self.name)

    def tree_string(self, level=0):
        current_indent = self._TREE_INDENT * level
        next_indent = self._TREE_INDENT * (level + 1)
        return (
            "{0}Entity name={2}\n"
            "{3}\n"
            "{4}".format(
                current_indent,
                next_indent,
                self.name,
                "\n".join([g.tree_string(level + 1) for g in self.generics]),
                "\n".join([p.tree_string(level + 1) for p in self.ports])))

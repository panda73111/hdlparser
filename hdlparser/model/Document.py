from model.HdlElement import HdlElement


class Document(HdlElement):
    def __init__(self):
        self.libraries = []
        self.imports = []
        self.entities = []

    def __str__(self):
        return "<Document entities={0}>".format([str(e) for e in self.entities])

    def tree_string(self, level=0):
        current_indent = self._TREE_INDENT * level
        next_indent = self._TREE_INDENT * (level + 1)  # type: str
        return (
            "{0}Document\n"
            "{1}libraries: {2}\n"
            "{1}imports: {3}\n"
            "{4}".format(
                current_indent,
                next_indent,
                ("\n           " + next_indent).join(self.libraries),
                ("\n         " + next_indent).join(self.imports),
                "\n".join([e.tree_string(level + 1) for e in self.entities])))

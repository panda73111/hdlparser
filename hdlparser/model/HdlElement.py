
class HdlElement:
    _TREE_INDENT = "  "

    def tree_string(self, level=0):
        self_str = str(self)[1:-1]
        return self._TREE_INDENT * level + self_str

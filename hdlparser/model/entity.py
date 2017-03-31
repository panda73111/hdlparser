from grammar.VhdlParser import VhdlParser
from model.hdl_element import HdlElement
from model.interface import GenericList
from model.port import PortList


class Entity(HdlElement):
    def __init__(self, name):
        self.name = name
        self.generics = []
        self.ports = []

    @classmethod
    def from_tree(cls, ctx: VhdlParser.Entity_declarationContext):
        name = ctx.identifier(0).getText()
        entity = cls(name)

        entity_header = ctx.entity_header()

        generic_clause = entity_header.generic_clause()
        port_clause = entity_header.port_clause()

        if generic_clause is not None:
            entity.generics = GenericList.from_tree(generic_clause)

        if port_clause is not None:
            entity.ports = PortList.from_tree(port_clause)

        return entity

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

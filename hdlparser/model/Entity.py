from model.HdlElement import HdlElement
from model.Interface import Interface
from model.Port import Port


class Entity(HdlElement):
    def __init__(self, name):
        self.name = name
        self.generics = []
        self.ports = []

    @classmethod
    def from_tree(cls, ctx):
        name = ctx.identifier(0).getText()
        entity = cls(name)

        entity_header = ctx.entity_header()

        generic_clause = entity_header.generic_clause()
        port_clause = entity_header.port_clause()

        if generic_clause is not None:

            generic_list = generic_clause.generic_list()

            for declaration in generic_list.interface_constant_declaration():

                data_type = declaration.subtype_indication().getText()
                value = declaration.expression()

                if value is not None:
                    value = value.getText()

                for identifier in declaration.identifier_list().identifier():
                    name = identifier.getText()
                    interface = Interface(name, data_type, value)
                    entity.generics.append(interface)

        if port_clause is not None:

            port_list = port_clause.port_list()
            interface_port_list = port_list.interface_port_list()

            for declaration in interface_port_list.interface_port_declaration():
                direction = declaration.signal_mode().getText()
                data_type = declaration.subtype_indication().getText()
                value = declaration.expression()

                if value is not None:
                    value = value.getText()

                for identifier in declaration.identifier_list().identifier():
                    name = identifier.getText()
                    interface = Interface(name, data_type, value)
                    port = Port(direction, interface)
                    entity.ports.append(port)

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

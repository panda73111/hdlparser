from grammar.VhdlParser import VhdlParser
from model.hdl_element import HdlElement


class GenericList(HdlElement, list):
    @classmethod
    def from_tree(cls, ctx: VhdlParser.Generic_clauseContext):
        generic_list = cls()

        for declaration in ctx.generic_list().interface_constant_declaration():

            data_type = declaration.subtype_indication().getText()
            value = declaration.expression()

            if value is not None:
                value = value.getText()

            for identifier in declaration.identifier_list().identifier():
                name = identifier.getText()

                interface = Interface(name, data_type, value)
                generic_list.append(interface)

        return generic_list


class Interface(HdlElement):
    def __init__(self, name, data_type, value=None):
        self.name = name
        self.data_type = data_type
        self.value = value

    def __str__(self):
        return (
            "<Interface "
            "name={0.name} "
            "data_type={0.data_type} "
            "value={0.value}>".format(self))

from enum import Enum

from grammar.VhdlParser import VhdlParser
from model.data_type import DataType
from model.hdl_element import HdlElement
from model.interface import Interface


class PortDirection(Enum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"


class PortList(list, HdlElement):
    @classmethod
    def from_tree(cls, ctx: VhdlParser.Port_clauseContext):
        port_list = cls()

        interface_port_list = ctx.port_list().interface_port_list()

        for declaration in interface_port_list.interface_port_declaration():
            direction = declaration.signal_mode().getText()
            data_type = declaration.subtype_indication()
            data_type = DataType.from_tree(data_type)
            value = declaration.expression()

            if value is not None:
                value = value.getText()

            for identifier in declaration.identifier_list().identifier():
                name = identifier.getText()
                interface = Interface(name, data_type, value)

                port = Port(direction, interface)
                port_list.append(port)

        return port_list


class Port(HdlElement):
    def __init__(self, direction, interface):
        self.direction = direction
        self.interface = interface

    def __str__(self):
        return (
            "<Port "
            "direction={0.direction} "
            "interface={0.interface}>".format(self))

from enum import Enum

from model.hdl_element import HdlElement


class PortDirection(Enum):
    IN = 0
    OUT = 1
    INOUT = 2


class Port(HdlElement):
    def __init__(self, direction, interface):
        self.direction = direction
        self.interface = interface

    def __str__(self):
        return (
            "<Port "
            "direction={0.direction} "
            "interface={0.interface}>".format(self))

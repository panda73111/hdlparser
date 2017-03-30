from enum import Enum


class PortDirection(Enum):
    IN = 0
    OUT = 1
    INOUT = 2


class Port:
    def __init__(self, direction, interface):
        self.direction = direction
        self.interface = interface

    def __str__(self):
        return (
            "[Port "
            "direction={s.direction} "
            "interface={s.interface}]".format(s=self))

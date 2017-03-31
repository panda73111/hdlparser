from model.HdlElement import HdlElement


class DataType(HdlElement):
    def __init__(self, identifiers, constraint=None):
        self.identifiers = identifiers
        self.constraint = constraint

    def __str__(self):
        return (
            "<DataType "
            "identifiers={0.identifiers} "
            "constraint={0.constraint}>".format(self))

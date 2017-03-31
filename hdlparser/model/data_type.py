from grammar.VhdlParser import VhdlParser
from model.constraint import Constraint
from model.hdl_element import HdlElement


class DataType(HdlElement):
    def __init__(self, identifier, constraint=None):
        self.identifier = identifier
        self.constraint = constraint

    @classmethod
    def from_tree(cls, ctx: VhdlParser.Subtype_indicationContext):
        identifier = ctx.selected_name(0).getText()
        constraint = ctx.constraint()

        if constraint is not None:
            constraint = Constraint.from_tree(constraint)

        return cls(identifier, constraint)

    def __str__(self):
        constraint_str = ""
        if self.constraint is not None:
            constraint_str = " " + str(self.constraint)

        return self.identifier + constraint_str

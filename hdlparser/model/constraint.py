from enum import Enum

from grammar.VhdlParser import VhdlParser
from model.hdl_element import HdlElement


class RangeConstraintDirection(HdlElement, Enum):
    TO = "to"
    DOWNTO = "downto"

    @classmethod
    def from_tree(cls, ctx: VhdlParser.DirectionContext):
        if ctx.TO() is not None:
            return cls.TO
        return cls.DOWNTO


class Constraint(HdlElement):
    @classmethod
    def from_tree(cls, ctx: VhdlParser.ConstraintContext):
        range_constraint = ctx.range_constraint()

        if range_constraint is not None:
            return RangeConstraint.from_tree(range_constraint)

        return IndexConstraint.from_tree(ctx.index_constraint())


class RangeConstraint(HdlElement):
    def __init__(self, left_bound, direction, right_bound):
        self.left_bound = left_bound
        self.direction = direction
        self.right_bound = right_bound

    @classmethod
    def from_tree(cls, ctx: VhdlParser.Range_constraintContext):
        range_base = ctx.range_base()

        explicit_range = range_base.explicit_range()
        name = range_base.name()

        if explicit_range is not None:

            bounds = [e.getText() for e in explicit_range.simple_expression()]
            direction = explicit_range.direction()
            direction = RangeConstraintDirection.from_tree(direction)

            return cls(bounds[0], direction, bounds[1])

        raise NotImplementedError

    def __str__(self):
        return "range {0.left_bound} {0.direction} {0.right_bound}".format(self)


class IndexConstraint(HdlElement):
    def __init__(self, ranges):
        self.ranges = ranges

    @classmethod
    def from_tree(cls, ctx: VhdlParser.Index_constraintContext):
        for discrete_range in ctx.discrete_range():
            range_base = discrete_range.range_base()
            subtype_indication = discrete_range.subtype_indication()

            if range_base is not None:


    def __str__(self):
        return "({0})".format(self.ranges)

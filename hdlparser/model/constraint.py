from model.hdl_element import HdlElement


class RangeConstraint(HdlElement):
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return (
            "<RangeConstraint "
            "lower_bound={0.lower_bound} "
            "upper_bound={0.upper_bound}>".format(self))


class IndexConstraint(HdlElement):
    def __init__(self, index):
        self.index = index

    def __str__(self):
        return (
            "<IndexConstraint "
            "upper_bound={0.index}>".format(self))

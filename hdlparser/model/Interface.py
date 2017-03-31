from model.HdlElement import HdlElement


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

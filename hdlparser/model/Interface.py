
class Interface:
    def __init__(self, name, data_type, value=None):
        self.name = name
        self.data_type = data_type
        self.value = value

    def __str__(self):
        return (
            "[Interface "
            "name={s.name} "
            "data_type={s.data_type} "
            "value={s.value}]".format(s=self))

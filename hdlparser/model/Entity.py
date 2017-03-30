
class Entity:
    def __init__(self, name):
        self.name = name
        self.generics = []
        self.ports = []

    def __str__(self):
        return "[Entity name={0}]".format(self.name)

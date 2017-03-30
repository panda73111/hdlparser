
class Document:
    def __init__(self):
        self.libraries = []
        self.imports = []
        self.entities = []

    def __str__(self):
        return "[Document entities={0}]".format(self.entities)

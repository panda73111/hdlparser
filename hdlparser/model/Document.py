from model.Entity import Entity
from model.HdlElement import HdlElement


class Document(HdlElement):
    def __init__(self):
        self.libraries = []
        self.imports = []
        self.entities = []
        self.architectures = []

    @classmethod
    def from_tree(cls, ctx):
        document = cls()

        for design_unit in ctx.design_unit():

            context_clause = design_unit.context_clause()
            library_unit = design_unit.library_unit()

            for context_item in context_clause.context_item():
                library_clause = context_item.library_clause()
                use_clause = context_item.use_clause()

                if library_clause is not None:

                    # libraries
                    for name in library_clause.logical_name_list().logical_name():
                        document.libraries.append(name.getText())

                elif use_clause is not None:

                    # 'use' imports
                    document.imports += [name_ctx.getText() for name_ctx in use_clause.selected_name()]

            primary_unit = library_unit.primary_unit()
            secondary_unit = library_unit.secondary_unit()

            if primary_unit is not None:

                entity_declaration = primary_unit.entity_declaration()
                configuration_declaration = primary_unit.configuration_declaration()
                package_declaration = primary_unit.package_declaration()

                if entity_declaration is not None:

                    # entity
                    entity = Entity.from_tree(entity_declaration)
                    document.entities.append(entity)

            elif secondary_unit is not None:

                architecture_body = secondary_unit.architecture_body()
                package_body = secondary_unit.package_body()

        return document

    def __str__(self):
        return "<Document entities={0}>".format([str(e) for e in self.entities])

    def tree_string(self, level=0):
        current_indent = self._TREE_INDENT * level
        next_indent = self._TREE_INDENT * (level + 1)  # type: str
        return (
            "{0}Document\n"
            "{1}libraries: {2}\n"
            "{1}imports: {3}\n"
            "{4}\n"
            "{5}".format(
                current_indent,
                next_indent,
                ("\n           " + next_indent).join(self.libraries),
                ("\n         " + next_indent).join(self.imports),
                "\n".join([e.tree_string(level + 1) for e in self.entities]),
                "\n".join([e.tree_string(level + 1) for e in self.architectures])))

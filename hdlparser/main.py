import logging
import sys

from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream

from hdlparser.grammar.VhdlLexer import VhdlLexer
from hdlparser.grammar.VhdlListener import VhdlListener
from hdlparser.grammar.VhdlParser import VhdlParser
from model.Document import Document
from model.Entity import Entity
from model.Interface import Interface
from model.Port import Port


class RebuildingVhdlListener(VhdlListener):
    def __init__(self):
        self._logger = logging.getLogger(__package__)
        self.document = Document()

    @staticmethod
    def _is_selected_name(ctx):
        return isinstance(ctx, VhdlParser.Selected_nameContext)

    @staticmethod
    def _is_constant_declaration(ctx):
        return isinstance(ctx, VhdlParser.Interface_constant_declarationContext)

    @staticmethod
    def _is_identifier(ctx):
        return isinstance(ctx, VhdlParser.IdentifierContext)

    @staticmethod
    def _is_port_declaration(ctx):
        return isinstance(ctx, VhdlParser.Interface_port_declarationContext)

    # library clause
    def enterLibrary_clause(self, ctx: VhdlParser.Library_clauseContext):
        for name_ctx in ctx.logical_name_list().children:
            self.document.libraries.append(name_ctx.getText())

    # use clause
    def enterUse_clause(self, ctx: VhdlParser.Use_clauseContext):
        name_ctx_children = ctx.getChildren(self._is_selected_name)
        self.document.imports += [name_ctx.getText() for name_ctx in name_ctx_children]

    # entity declaration
    def enterEntity_declaration(self, ctx: VhdlParser.Entity_declarationContext):
        entity_name = ctx.identifier(0).getText()
        self.document.entities.append(Entity(entity_name))

    # generic list
    def enterGeneric_list(self, ctx:VhdlParser.Generic_listContext):
        entity = self.document.entities[-1]

        for generic_ctx in ctx.getChildren(self._is_constant_declaration):
            data_type = generic_ctx.subtype_indication().getText()
            value = generic_ctx.expression()
            if value is not None:
                value = value.getText()

            for identifier_ctx in generic_ctx.identifier_list().getChildren(self._is_identifier):
                name = identifier_ctx.getText()
                interface = Interface(name, data_type, value)
                entity.generics.append(interface)

    # port list
    def enterInterface_port_list(self, ctx: VhdlParser.Interface_port_listContext):
        entity = self.document.entities[-1]

        for port_ctx in ctx.getChildren(self._is_port_declaration):
            direction = port_ctx.signal_mode().getText()
            data_type = port_ctx.subtype_indication().getText()
            value = port_ctx.expression()
            if value is not None:
                value = value.getText()

            for identifier_ctx in port_ctx.identifier_list().getChildren(self._is_identifier):
                name = identifier_ctx.getText()
                interface = Interface(name, data_type, value)
                port = Port(direction, interface)
                entity.ports.append(port)


def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    file_stream = FileStream(r"D:\Eigene Dateien\git\pandaLight-HDL\LED_CONTROL\LED_CONTROL.vhd")

    lexer = VhdlLexer(file_stream)
    token_stream = CommonTokenStream(lexer)
    parser = VhdlParser(token_stream)

    listener = RebuildingVhdlListener()
    tree = parser.design_file()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    pass


if __name__ == "__main__":
    main()

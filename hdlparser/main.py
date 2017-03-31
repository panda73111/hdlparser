import logging
import sys

from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream

from hdlparser.grammar.VhdlLexer import VhdlLexer
from hdlparser.grammar.VhdlListener import VhdlListener
from hdlparser.grammar.VhdlParser import VhdlParser
from model.document import Document


def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    file_stream = FileStream(
        r"D:\Eigene Dateien\git\pandaLight-HDL"
        r"\pandaLight-tests\complete LED test\PANDA_LIGHT.vhd")

    lexer = VhdlLexer(file_stream)
    token_stream = CommonTokenStream(lexer)
    parser = VhdlParser(token_stream)

    listener = VhdlListener()
    tree = parser.design_file()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(Document.from_tree(tree).tree_string())


if __name__ == "__main__":
    main()

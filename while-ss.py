import sys
from antlr4 import *
from dist.WhileLexer import WhileLexer
from dist.WhileParser import WhileParser
from dist.WhileVisitor import WhileVisitor
from interpreter import Interpreter


def main():
    val = InputStream(input())
    lexer = WhileLexer(val)
    stream = CommonTokenStream(lexer)
    parser = WhileParser(stream)
    tree = parser.compileUnit()
    ast = WhileVisitor().visitCompileUnit(tree)
    interpreter = Interpreter()
    interpreter.eval(ast)
    interpreter.print_result()
    return


if __name__ == '__main__':
    main()

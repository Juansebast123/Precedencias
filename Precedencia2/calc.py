import sys
from antlr4 import *
from LabeledExpr2Lexer import LabeledExpr2Lexer
from LabeledExpr2Parser import LabeledExpr2Parser
from EvalVisitor import EvalVisitor

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = LabeledExpr2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LabeledExpr2Parser(stream)
    tree = parser.prog()

    evalv = EvalVisitor()
    evalv.visit(tree)

if __name__ == '__main__':
    main()

# Generated from LabeledExpr.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\6\n/\n\n\r\n\16\n\60\3\13\6\13\64")
        buf.write("\n\13\r\13\16\13\65\3\13\3\13\6\13:\n\13\r\13\16\13;\3")
        buf.write("\f\6\f?\n\f\r\f\16\f@\3\r\5\rD\n\r\3\r\3\r\3\16\6\16I")
        buf.write("\n\16\r\16\16\16J\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\5\4\2")
        buf.write("C\\c|\3\2\62;\4\2\13\13\"\"\2S\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2")
        buf.write("\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17")
        buf.write(")\3\2\2\2\21+\3\2\2\2\23.\3\2\2\2\25\63\3\2\2\2\27>\3")
        buf.write("\2\2\2\31C\3\2\2\2\33H\3\2\2\2\35\36\7?\2\2\36\4\3\2\2")
        buf.write("\2\37 \7*\2\2 \6\3\2\2\2!\"\7+\2\2\"\b\3\2\2\2#$\7#\2")
        buf.write("\2$\n\3\2\2\2%&\7,\2\2&\f\3\2\2\2\'(\7\61\2\2(\16\3\2")
        buf.write("\2\2)*\7-\2\2*\20\3\2\2\2+,\7/\2\2,\22\3\2\2\2-/\t\2\2")
        buf.write("\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\24\3\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2\64\65\3\2\2\2")
        buf.write("\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\679\7\60\2")
        buf.write("\28:\t\3\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<")
        buf.write("\26\3\2\2\2=?\t\3\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A")
        buf.write("\3\2\2\2A\30\3\2\2\2BD\7\17\2\2CB\3\2\2\2CD\3\2\2\2DE")
        buf.write("\3\2\2\2EF\7\f\2\2F\32\3\2\2\2GI\t\4\2\2HG\3\2\2\2IJ\3")
        buf.write("\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\b\16\2\2M\34\3")
        buf.write("\2\2\2\t\2\60\65;@CJ\3\b\2\2")
        return buf.getvalue()


class LabeledExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    MUL = 5
    DIV = 6
    ADD = 7
    SUB = 8
    ID = 9
    FLOAT = 10
    INT = 11
    NEWLINE = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'!'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "ID", "FLOAT", "INT", "NEWLINE", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "MUL", "DIV", "ADD", "SUB", 
                  "ID", "FLOAT", "INT", "NEWLINE", "WS" ]

    grammarFileName = "LabeledExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



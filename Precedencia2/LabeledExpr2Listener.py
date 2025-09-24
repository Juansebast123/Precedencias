# Generated from LabeledExpr2.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LabeledExpr2Parser import LabeledExpr2Parser
else:
    from LabeledExpr2Parser import LabeledExpr2Parser

# This class defines a complete listener for a parse tree produced by LabeledExpr2Parser.
class LabeledExpr2Listener(ParseTreeListener):

    # Enter a parse tree produced by LabeledExpr2Parser#prog.
    def enterProg(self, ctx:LabeledExpr2Parser.ProgContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#prog.
    def exitProg(self, ctx:LabeledExpr2Parser.ProgContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#printExpr.
    def enterPrintExpr(self, ctx:LabeledExpr2Parser.PrintExprContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#printExpr.
    def exitPrintExpr(self, ctx:LabeledExpr2Parser.PrintExprContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#assign.
    def enterAssign(self, ctx:LabeledExpr2Parser.AssignContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#assign.
    def exitAssign(self, ctx:LabeledExpr2Parser.AssignContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#blank.
    def enterBlank(self, ctx:LabeledExpr2Parser.BlankContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#blank.
    def exitBlank(self, ctx:LabeledExpr2Parser.BlankContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#parens.
    def enterParens(self, ctx:LabeledExpr2Parser.ParensContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#parens.
    def exitParens(self, ctx:LabeledExpr2Parser.ParensContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#AddSub.
    def enterAddSub(self, ctx:LabeledExpr2Parser.AddSubContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#AddSub.
    def exitAddSub(self, ctx:LabeledExpr2Parser.AddSubContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#MulDiv.
    def enterMulDiv(self, ctx:LabeledExpr2Parser.MulDivContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#MulDiv.
    def exitMulDiv(self, ctx:LabeledExpr2Parser.MulDivContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#function.
    def enterFunction(self, ctx:LabeledExpr2Parser.FunctionContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#function.
    def exitFunction(self, ctx:LabeledExpr2Parser.FunctionContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#factorial.
    def enterFactorial(self, ctx:LabeledExpr2Parser.FactorialContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#factorial.
    def exitFactorial(self, ctx:LabeledExpr2Parser.FactorialContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#id.
    def enterId(self, ctx:LabeledExpr2Parser.IdContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#id.
    def exitId(self, ctx:LabeledExpr2Parser.IdContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#float.
    def enterFloat(self, ctx:LabeledExpr2Parser.FloatContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#float.
    def exitFloat(self, ctx:LabeledExpr2Parser.FloatContext):
        pass


    # Enter a parse tree produced by LabeledExpr2Parser#int.
    def enterInt(self, ctx:LabeledExpr2Parser.IntContext):
        pass

    # Exit a parse tree produced by LabeledExpr2Parser#int.
    def exitInt(self, ctx:LabeledExpr2Parser.IntContext):
        pass



del LabeledExpr2Parser
# Generated from LabeledExpr2.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LabeledExpr2Parser import LabeledExpr2Parser
else:
    from LabeledExpr2Parser import LabeledExpr2Parser

# This class defines a complete generic visitor for a parse tree produced by LabeledExpr2Parser.

class LabeledExpr2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by LabeledExpr2Parser#prog.
    def visitProg(self, ctx:LabeledExpr2Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#printExpr.
    def visitPrintExpr(self, ctx:LabeledExpr2Parser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#assign.
    def visitAssign(self, ctx:LabeledExpr2Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#blank.
    def visitBlank(self, ctx:LabeledExpr2Parser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#parens.
    def visitParens(self, ctx:LabeledExpr2Parser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#AddSub.
    def visitAddSub(self, ctx:LabeledExpr2Parser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#MulDiv.
    def visitMulDiv(self, ctx:LabeledExpr2Parser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#function.
    def visitFunction(self, ctx:LabeledExpr2Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#factorial.
    def visitFactorial(self, ctx:LabeledExpr2Parser.FactorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#id.
    def visitId(self, ctx:LabeledExpr2Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#float.
    def visitFloat(self, ctx:LabeledExpr2Parser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExpr2Parser#int.
    def visitInt(self, ctx:LabeledExpr2Parser.IntContext):
        return self.visitChildren(ctx)



del LabeledExpr2Parser
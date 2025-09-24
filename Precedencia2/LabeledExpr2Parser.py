# Generated from LabeledExpr2.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4")
        buf.write("\63\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2\t\n\3\2\7\b\2;\2\t")
        buf.write("\3\2\2\2\4\26\3\2\2\2\6%\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2")
        buf.write("\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2")
        buf.write("\r\16\5\6\4\2\16\17\7\16\2\2\17\27\3\2\2\2\20\21\7\13")
        buf.write("\2\2\21\22\7\3\2\2\22\23\5\6\4\2\23\24\7\16\2\2\24\27")
        buf.write("\3\2\2\2\25\27\7\16\2\2\26\r\3\2\2\2\26\20\3\2\2\2\26")
        buf.write("\25\3\2\2\2\27\5\3\2\2\2\30\31\b\4\1\2\31&\7\f\2\2\32")
        buf.write("&\7\r\2\2\33&\7\13\2\2\34\35\7\4\2\2\35\36\5\6\4\2\36")
        buf.write("\37\7\5\2\2\37&\3\2\2\2 !\7\13\2\2!\"\7\4\2\2\"#\5\6\4")
        buf.write("\2#$\7\5\2\2$&\3\2\2\2%\30\3\2\2\2%\32\3\2\2\2%\33\3\2")
        buf.write("\2\2%\34\3\2\2\2% \3\2\2\2&\61\3\2\2\2\'(\f\n\2\2()\t")
        buf.write("\2\2\2)\60\5\6\4\13*+\f\t\2\2+,\t\3\2\2,\60\5\6\4\n-.")
        buf.write("\f\3\2\2.\60\7\6\2\2/\'\3\2\2\2/*\3\2\2\2/-\3\2\2\2\60")
        buf.write("\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\7\3\2\2\2\63")
        buf.write("\61\3\2\2\2\7\13\26%/\61")
        return buf.getvalue()


class LabeledExpr2Parser ( Parser ):

    grammarFileName = "LabeledExpr2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'!'", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MUL", "DIV", "ADD", "SUB", "ID", "FLOAT", 
                      "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    MUL=5
    DIV=6
    ADD=7
    SUB=8
    ID=9
    FLOAT=10
    INT=11
    NEWLINE=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExpr2Parser.StatContext)
            else:
                return self.getTypedRuleContext(LabeledExpr2Parser.StatContext,i)


        def getRuleIndex(self):
            return LabeledExpr2Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LabeledExpr2Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LabeledExpr2Parser.T__1) | (1 << LabeledExpr2Parser.ID) | (1 << LabeledExpr2Parser.FLOAT) | (1 << LabeledExpr2Parser.INT) | (1 << LabeledExpr2Parser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExpr2Parser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(LabeledExpr2Parser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LabeledExpr2Parser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExpr2Parser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LabeledExpr2Parser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = LabeledExpr2Parser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = LabeledExpr2Parser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(LabeledExpr2Parser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = LabeledExpr2Parser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(LabeledExpr2Parser.ID)
                self.state = 15
                self.match(LabeledExpr2Parser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(LabeledExpr2Parser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = LabeledExpr2Parser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(LabeledExpr2Parser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExpr2Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExpr2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,i)

        def ADD(self):
            return self.getToken(LabeledExpr2Parser.ADD, 0)
        def SUB(self):
            return self.getToken(LabeledExpr2Parser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExpr2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,i)

        def MUL(self):
            return self.getToken(LabeledExpr2Parser.MUL, 0)
        def DIV(self):
            return self.getToken(LabeledExpr2Parser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class FunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.func = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,0)

        def ID(self):
            return self.getToken(LabeledExpr2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)


    class FactorialContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExpr2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorial" ):
                listener.enterFactorial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorial" ):
                listener.exitFactorial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorial" ):
                return visitor.visitFactorial(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExpr2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(LabeledExpr2Parser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExpr2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LabeledExpr2Parser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LabeledExpr2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LabeledExpr2Parser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(LabeledExpr2Parser.FLOAT)
                pass

            elif la_ == 2:
                localctx = LabeledExpr2Parser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(LabeledExpr2Parser.INT)
                pass

            elif la_ == 3:
                localctx = LabeledExpr2Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(LabeledExpr2Parser.ID)
                pass

            elif la_ == 4:
                localctx = LabeledExpr2Parser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(LabeledExpr2Parser.T__1)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(LabeledExpr2Parser.T__2)
                pass

            elif la_ == 5:
                localctx = LabeledExpr2Parser.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                localctx.func = self.match(LabeledExpr2Parser.ID)
                self.state = 31
                self.match(LabeledExpr2Parser.T__1)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(LabeledExpr2Parser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LabeledExpr2Parser.AddSubContext(self, LabeledExpr2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 38
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExpr2Parser.ADD or _la==LabeledExpr2Parser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LabeledExpr2Parser.MulDivContext(self, LabeledExpr2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExpr2Parser.MUL or _la==LabeledExpr2Parser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LabeledExpr2Parser.FactorialContext(self, LabeledExpr2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 44
                        self.match(LabeledExpr2Parser.T__3)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         





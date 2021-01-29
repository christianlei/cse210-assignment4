# Generated from While.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3\3\4\3")
        buf.write("\4\3\4\5\4\35\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5,\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5=\n\5\f\5\16\5@\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6O\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7]\n\7\3\7\2\3\b\b\2\4\6\b\n\f\2\6\3\2\b\t\3\2")
        buf.write("\23\24\4\2\f\f\20\20\3\2\16\17\2h\2\16\3\2\2\2\4\21\3")
        buf.write("\2\2\2\6\34\3\2\2\2\b+\3\2\2\2\nN\3\2\2\2\f\\\3\2\2\2")
        buf.write("\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\26\5\6\4")
        buf.write("\2\22\23\7\7\2\2\23\25\5\6\4\2\24\22\3\2\2\2\25\30\3\2")
        buf.write("\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\5\3\2\2\2\30\26\3")
        buf.write("\2\2\2\31\35\5\f\7\2\32\35\5\n\6\2\33\35\5\b\5\2\34\31")
        buf.write("\3\2\2\2\34\32\3\2\2\2\34\33\3\2\2\2\35\7\3\2\2\2\36\37")
        buf.write("\b\5\1\2\37 \7\3\2\2 !\5\b\5\2!\"\7\4\2\2\",\3\2\2\2#")
        buf.write("$\t\2\2\2$,\5\b\5\r%&\7\r\2\2&,\5\b\5\b\',\7\34\2\2(,")
        buf.write("\7\33\2\2),\t\3\2\2*,\7\32\2\2+\36\3\2\2\2+#\3\2\2\2+")
        buf.write("%\3\2\2\2+\'\3\2\2\2+(\3\2\2\2+)\3\2\2\2+*\3\2\2\2,>\3")
        buf.write("\2\2\2-.\f\f\2\2./\7\n\2\2/=\5\b\5\r\60\61\f\13\2\2\61")
        buf.write("\62\t\2\2\2\62=\5\b\5\f\63\64\f\n\2\2\64\65\t\4\2\2\65")
        buf.write("=\5\b\5\13\66\67\f\t\2\2\678\t\5\2\28=\5\b\5\n9:\f\7\2")
        buf.write("\2:;\7\13\2\2;=\5\b\5\b<-\3\2\2\2<\60\3\2\2\2<\63\3\2")
        buf.write("\2\2<\66\3\2\2\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2")
        buf.write("\2?\t\3\2\2\2@>\3\2\2\2AB\7\25\2\2BC\5\b\5\2CD\7\26\2")
        buf.write("\2DE\5\6\4\2EF\7\27\2\2FG\5\6\4\2GO\3\2\2\2HI\5\b\5\2")
        buf.write("IJ\7\21\2\2JK\5\6\4\2KL\7\22\2\2LM\5\6\4\2MO\3\2\2\2N")
        buf.write("A\3\2\2\2NH\3\2\2\2O\13\3\2\2\2PQ\7\30\2\2QR\5\b\5\2R")
        buf.write("S\7\31\2\2ST\7\5\2\2TU\5\4\3\2UV\7\6\2\2V]\3\2\2\2WX\7")
        buf.write("\30\2\2XY\5\b\5\2YZ\7\31\2\2Z[\5\6\4\2[]\3\2\2\2\\P\3")
        buf.write("\2\2\2\\W\3\2\2\2]\r\3\2\2\2\t\26\34+<>N\\")
        return buf.getvalue()


class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "':='", "'='", "'\u00AC'", "'\u2227'", 
                     "'\u2228'", "'<'", "'?'", "':'", "'true'", "'false'", 
                     "'if'", "'then'", "'else'", "'while'", "'do'", "'skip'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SEMI", "OP_ADD", "OP_SUB", "OP_MUL", 
                      "OP_ASGN", "OP_EQ", "OP_NOT", "OP_AND", "OP_OR", "OP_LESS", 
                      "TERNARY_IF", "TERNARY_ELSE", "TRUE", "FALSE", "IF", 
                      "THEN", "ELSE", "WHILE", "DO", "PASS", "VAR", "NUMBER", 
                      "WS" ]

    RULE_compileUnit = 0
    RULE_semi_stat = 1
    RULE_stat = 2
    RULE_expr = 3
    RULE_if_stat = 4
    RULE_while_stat = 5

    ruleNames =  [ "compileUnit", "semi_stat", "stat", "expr", "if_stat", 
                   "while_stat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SEMI=5
    OP_ADD=6
    OP_SUB=7
    OP_MUL=8
    OP_ASGN=9
    OP_EQ=10
    OP_NOT=11
    OP_AND=12
    OP_OR=13
    OP_LESS=14
    TERNARY_IF=15
    TERNARY_ELSE=16
    TRUE=17
    FALSE=18
    IF=19
    THEN=20
    ELSE=21
    WHILE=22
    DO=23
    PASS=24
    VAR=25
    NUMBER=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompileUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def semi_stat(self):
            return self.getTypedRuleContext(WhileParser.Semi_statContext,0)


        def EOF(self):
            return self.getToken(WhileParser.EOF, 0)

        def getRuleIndex(self):
            return WhileParser.RULE_compileUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompileUnit" ):
                listener.enterCompileUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompileUnit" ):
                listener.exitCompileUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompileUnit" ):
                return visitor.visitCompileUnit(self)
            else:
                return visitor.visitChildren(self)




    def compileUnit(self):

        localctx = WhileParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.semi_stat()
            self.state = 13
            self.match(WhileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Semi_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.StatContext)
            else:
                return self.getTypedRuleContext(WhileParser.StatContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(WhileParser.SEMI)
            else:
                return self.getToken(WhileParser.SEMI, i)

        def getRuleIndex(self):
            return WhileParser.RULE_semi_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemi_stat" ):
                listener.enterSemi_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemi_stat" ):
                listener.exitSemi_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemi_stat" ):
                return visitor.visitSemi_stat(self)
            else:
                return visitor.visitChildren(self)




    def semi_stat(self):

        localctx = WhileParser.Semi_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_semi_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.stat()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WhileParser.SEMI:
                self.state = 16
                self.match(WhileParser.SEMI)
                self.state = 17
                self.stat()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def while_stat(self):
            return self.getTypedRuleContext(WhileParser.While_statContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(WhileParser.If_statContext,0)


        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def getRuleIndex(self):
            return WhileParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = WhileParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.while_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.if_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.expr(0)
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
            return WhileParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VALContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(WhileParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVAL" ):
                listener.enterVAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVAL" ):
                listener.exitVAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVAL" ):
                return visitor.visitVAL(self)
            else:
                return visitor.visitChildren(self)


    class PASSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def PASS(self):
            return self.getToken(WhileParser.PASS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPASS" ):
                listener.enterPASS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPASS" ):
                listener.exitPASS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPASS" ):
                return visitor.visitPASS(self)
            else:
                return visitor.visitChildren(self)


    class UNARYBOOLContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)

        def OP_NOT(self):
            return self.getToken(WhileParser.OP_NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUNARYBOOL" ):
                listener.enterUNARYBOOL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUNARYBOOL" ):
                listener.exitUNARYBOOL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUNARYBOOL" ):
                return visitor.visitUNARYBOOL(self)
            else:
                return visitor.visitChildren(self)


    class BOOLContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(WhileParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(WhileParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBOOL" ):
                listener.enterBOOL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBOOL" ):
                listener.exitBOOL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBOOL" ):
                return visitor.visitBOOL(self)
            else:
                return visitor.visitChildren(self)


    class INFIXContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)

        def OP_MUL(self):
            return self.getToken(WhileParser.OP_MUL, 0)
        def OP_ADD(self):
            return self.getToken(WhileParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(WhileParser.OP_SUB, 0)
        def OP_EQ(self):
            return self.getToken(WhileParser.OP_EQ, 0)
        def OP_LESS(self):
            return self.getToken(WhileParser.OP_LESS, 0)
        def OP_AND(self):
            return self.getToken(WhileParser.OP_AND, 0)
        def OP_OR(self):
            return self.getToken(WhileParser.OP_OR, 0)
        def OP_ASGN(self):
            return self.getToken(WhileParser.OP_ASGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINFIX" ):
                listener.enterINFIX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINFIX" ):
                listener.exitINFIX(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINFIX" ):
                return visitor.visitINFIX(self)
            else:
                return visitor.visitChildren(self)


    class PARENGRPContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPARENGRP" ):
                listener.enterPARENGRP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPARENGRP" ):
                listener.exitPARENGRP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPARENGRP" ):
                return visitor.visitPARENGRP(self)
            else:
                return visitor.visitChildren(self)


    class UNARYContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)

        def OP_ADD(self):
            return self.getToken(WhileParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(WhileParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUNARY" ):
                listener.enterUNARY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUNARY" ):
                listener.exitUNARY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUNARY" ):
                return visitor.visitUNARY(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(WhileParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINT" ):
                listener.enterINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINT" ):
                listener.exitINT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.T__0]:
                localctx = WhileParser.PARENGRPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 29
                self.match(WhileParser.T__0)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(WhileParser.T__1)
                pass
            elif token in [WhileParser.OP_ADD, WhileParser.OP_SUB]:
                localctx = WhileParser.UNARYContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==WhileParser.OP_ADD or _la==WhileParser.OP_SUB):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 34
                self.expr(11)
                pass
            elif token in [WhileParser.OP_NOT]:
                localctx = WhileParser.UNARYBOOLContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                localctx.op = self.match(WhileParser.OP_NOT)
                self.state = 36
                self.expr(6)
                pass
            elif token in [WhileParser.NUMBER]:
                localctx = WhileParser.INTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                localctx.value = self.match(WhileParser.NUMBER)
                pass
            elif token in [WhileParser.VAR]:
                localctx = WhileParser.VALContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                localctx.value = self.match(WhileParser.VAR)
                pass
            elif token in [WhileParser.TRUE, WhileParser.FALSE]:
                localctx = WhileParser.BOOLContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                localctx.value = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==WhileParser.TRUE or _la==WhileParser.FALSE):
                    localctx.value = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [WhileParser.PASS]:
                localctx = WhileParser.PASSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                localctx.value = self.match(WhileParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 44
                        localctx.op = self.match(WhileParser.OP_MUL)
                        self.state = 45
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 47
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.OP_ADD or _la==WhileParser.OP_SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.OP_EQ or _la==WhileParser.OP_LESS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.OP_AND or _la==WhileParser.OP_OR):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        localctx.op = self.match(WhileParser.OP_ASGN)
                        self.state = 57
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.conditional = None # ExprContext
            self.true = None # StatContext
            self.false = None # StatContext

        def IF(self):
            return self.getToken(WhileParser.IF, 0)

        def THEN(self):
            return self.getToken(WhileParser.THEN, 0)

        def ELSE(self):
            return self.getToken(WhileParser.ELSE, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.StatContext)
            else:
                return self.getTypedRuleContext(WhileParser.StatContext,i)


        def TERNARY_IF(self):
            return self.getToken(WhileParser.TERNARY_IF, 0)

        def TERNARY_ELSE(self):
            return self.getToken(WhileParser.TERNARY_ELSE, 0)

        def getRuleIndex(self):
            return WhileParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stat" ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = WhileParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_stat)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(WhileParser.IF)
                self.state = 64
                localctx.conditional = self.expr(0)
                self.state = 65
                self.match(WhileParser.THEN)
                self.state = 66
                localctx.true = self.stat()
                self.state = 67
                self.match(WhileParser.ELSE)
                self.state = 68
                localctx.false = self.stat()
                pass
            elif token in [WhileParser.T__0, WhileParser.OP_ADD, WhileParser.OP_SUB, WhileParser.OP_NOT, WhileParser.TRUE, WhileParser.FALSE, WhileParser.PASS, WhileParser.VAR, WhileParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                localctx.conditional = self.expr(0)
                self.state = 71
                self.match(WhileParser.TERNARY_IF)
                self.state = 72
                localctx.true = self.stat()
                self.state = 73
                self.match(WhileParser.TERNARY_ELSE)
                self.state = 74
                localctx.false = self.stat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_while_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NOPARENContext(While_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.While_statContext
            super().__init__(parser)
            self.conditional = None # ExprContext
            self.inner_no_brace = None # StatContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(WhileParser.WHILE, 0)
        def DO(self):
            return self.getToken(WhileParser.DO, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)

        def stat(self):
            return self.getTypedRuleContext(WhileParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNOPAREN" ):
                listener.enterNOPAREN(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNOPAREN" ):
                listener.exitNOPAREN(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNOPAREN" ):
                return visitor.visitNOPAREN(self)
            else:
                return visitor.visitChildren(self)


    class PARENWHILEBLOCKContext(While_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.While_statContext
            super().__init__(parser)
            self.conditional = None # ExprContext
            self.inner = None # Semi_statContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(WhileParser.WHILE, 0)
        def DO(self):
            return self.getToken(WhileParser.DO, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)

        def semi_stat(self):
            return self.getTypedRuleContext(WhileParser.Semi_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPARENWHILEBLOCK" ):
                listener.enterPARENWHILEBLOCK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPARENWHILEBLOCK" ):
                listener.exitPARENWHILEBLOCK(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPARENWHILEBLOCK" ):
                return visitor.visitPARENWHILEBLOCK(self)
            else:
                return visitor.visitChildren(self)



    def while_stat(self):

        localctx = WhileParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while_stat)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = WhileParser.PARENWHILEBLOCKContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(WhileParser.WHILE)
                self.state = 79
                localctx.conditional = self.expr(0)
                self.state = 80
                self.match(WhileParser.DO)
                self.state = 81
                self.match(WhileParser.T__2)
                self.state = 82
                localctx.inner = self.semi_stat()
                self.state = 83
                self.match(WhileParser.T__3)
                pass

            elif la_ == 2:
                localctx = WhileParser.NOPARENContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(WhileParser.WHILE)
                self.state = 86
                localctx.conditional = self.expr(0)
                self.state = 87
                self.match(WhileParser.DO)
                self.state = 88
                localctx.inner_no_brace = self.stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         





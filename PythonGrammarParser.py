# Generated from PythonGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,60,8,3,10,3,12,3,63,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,4,3,4,82,8,4,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,3,6,93,8,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,
        7,102,8,7,10,7,12,7,105,9,7,1,8,1,8,1,8,4,8,110,8,8,11,8,12,8,111,
        1,8,1,8,1,8,3,8,117,8,8,1,9,1,9,3,9,121,8,9,1,9,0,1,6,10,0,2,4,6,
        8,10,12,14,16,18,0,3,1,0,2,3,1,0,4,5,1,0,6,9,131,0,24,1,0,0,0,2,
        34,1,0,0,0,4,36,1,0,0,0,6,48,1,0,0,0,8,64,1,0,0,0,10,83,1,0,0,0,
        12,88,1,0,0,0,14,98,1,0,0,0,16,116,1,0,0,0,18,118,1,0,0,0,20,23,
        3,2,1,0,21,23,3,12,6,0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,
        24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,
        0,0,1,28,1,1,0,0,0,29,35,3,4,2,0,30,35,3,6,3,0,31,35,3,8,4,0,32,
        35,3,10,5,0,33,35,3,18,9,0,34,29,1,0,0,0,34,30,1,0,0,0,34,31,1,0,
        0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,0,36,37,5,20,0,0,37,38,
        5,1,0,0,38,39,3,6,3,0,39,5,1,0,0,0,40,41,6,3,-1,0,41,42,5,10,0,0,
        42,43,3,6,3,0,43,44,5,11,0,0,44,49,1,0,0,0,45,49,5,20,0,0,46,49,
        5,21,0,0,47,49,5,22,0,0,48,40,1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,
        0,48,47,1,0,0,0,49,61,1,0,0,0,50,51,10,7,0,0,51,52,7,0,0,0,52,60,
        3,6,3,8,53,54,10,6,0,0,54,55,7,1,0,0,55,60,3,6,3,7,56,57,10,5,0,
        0,57,58,7,2,0,0,58,60,3,6,3,6,59,50,1,0,0,0,59,53,1,0,0,0,59,56,
        1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,7,1,0,0,0,63,
        61,1,0,0,0,64,65,5,12,0,0,65,66,3,6,3,0,66,67,5,13,0,0,67,75,3,16,
        8,0,68,69,5,14,0,0,69,70,3,6,3,0,70,71,5,13,0,0,71,72,3,16,8,0,72,
        74,1,0,0,0,73,68,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,
        0,76,81,1,0,0,0,77,75,1,0,0,0,78,79,5,15,0,0,79,80,5,13,0,0,80,82,
        3,16,8,0,81,78,1,0,0,0,81,82,1,0,0,0,82,9,1,0,0,0,83,84,5,16,0,0,
        84,85,3,6,3,0,85,86,5,13,0,0,86,87,3,16,8,0,87,11,1,0,0,0,88,89,
        5,17,0,0,89,90,5,20,0,0,90,92,5,10,0,0,91,93,3,14,7,0,92,91,1,0,
        0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,11,0,0,95,96,5,13,0,0,96,
        97,3,16,8,0,97,13,1,0,0,0,98,103,5,20,0,0,99,100,5,18,0,0,100,102,
        5,20,0,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,
        1,0,0,0,104,15,1,0,0,0,105,103,1,0,0,0,106,107,5,23,0,0,107,109,
        5,24,0,0,108,110,3,2,1,0,109,108,1,0,0,0,110,111,1,0,0,0,111,109,
        1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,5,25,0,0,114,117,
        1,0,0,0,115,117,3,2,1,0,116,106,1,0,0,0,116,115,1,0,0,0,117,17,1,
        0,0,0,118,120,5,19,0,0,119,121,3,6,3,0,120,119,1,0,0,0,120,121,1,
        0,0,0,121,19,1,0,0,0,13,22,24,34,48,59,61,75,81,92,103,111,116,120
    ]

class PythonGrammarParser ( Parser ):

    grammarFileName = "PythonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'=='", 
                     "'!='", "'<'", "'>'", "'('", "')'", "'if'", "':'", 
                     "'elif'", "'else'", "'while'", "'def'", "','", "'return'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'    '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "STRING", "NEWLINE", "INDENT", "DEDENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_if_statement = 4
    RULE_while_statement = 5
    RULE_function_def = 6
    RULE_parameters = 7
    RULE_block = 8
    RULE_return_statement = 9

    ruleNames =  [ "program", "statement", "assignment", "expression", "if_statement", 
                   "while_statement", "function_def", "parameters", "block", 
                   "return_statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    NUMBER=21
    STRING=22
    NEWLINE=23
    INDENT=24
    DEDENT=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonGrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.StatementContext,i)


        def function_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.Function_defContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.Function_defContext,i)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PythonGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8066048) != 0):
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 12, 16, 19, 20, 21, 22]:
                    self.state = 20
                    self.statement()
                    pass
                elif token in [17]:
                    self.state = 21
                    self.function_def()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(PythonGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PythonGrammarParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(PythonGrammarParser.ExpressionContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(PythonGrammarParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(PythonGrammarParser.While_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(PythonGrammarParser.Return_statementContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PythonGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.while_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonGrammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(PythonGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PythonGrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(PythonGrammarParser.ID)
            self.state = 37
            self.match(PythonGrammarParser.T__0)
            self.state = 38
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.ExpressionContext,i)


        def ID(self):
            return self.getToken(PythonGrammarParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PythonGrammarParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PythonGrammarParser.STRING, 0)

        def getRuleIndex(self):
            return PythonGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 41
                self.match(PythonGrammarParser.T__9)
                self.state = 42
                self.expression(0)
                self.state = 43
                self.match(PythonGrammarParser.T__10)
                pass
            elif token in [20]:
                self.state = 45
                self.match(PythonGrammarParser.ID)
                pass
            elif token in [21]:
                self.state = 46
                self.match(PythonGrammarParser.NUMBER)
                pass
            elif token in [22]:
                self.state = 47
                self.match(PythonGrammarParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PythonGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 51
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 54
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 57
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        self.expression(6)
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.BlockContext,i)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = PythonGrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(PythonGrammarParser.T__11)
            self.state = 65
            self.expression(0)
            self.state = 66
            self.match(PythonGrammarParser.T__12)
            self.state = 67
            self.block()
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.match(PythonGrammarParser.T__13)
                    self.state = 69
                    self.expression(0)
                    self.state = 70
                    self.match(PythonGrammarParser.T__12)
                    self.state = 71
                    self.block() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(PythonGrammarParser.T__14)
                self.state = 79
                self.match(PythonGrammarParser.T__12)
                self.state = 80
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PythonGrammarParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(PythonGrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = PythonGrammarParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(PythonGrammarParser.T__15)
            self.state = 84
            self.expression(0)
            self.state = 85
            self.match(PythonGrammarParser.T__12)
            self.state = 86
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonGrammarParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(PythonGrammarParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(PythonGrammarParser.ParametersContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = PythonGrammarParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(PythonGrammarParser.T__16)
            self.state = 89
            self.match(PythonGrammarParser.ID)
            self.state = 90
            self.match(PythonGrammarParser.T__9)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 91
                self.parameters()


            self.state = 94
            self.match(PythonGrammarParser.T__10)
            self.state = 95
            self.match(PythonGrammarParser.T__12)
            self.state = 96
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonGrammarParser.ID)
            else:
                return self.getToken(PythonGrammarParser.ID, i)

        def getRuleIndex(self):
            return PythonGrammarParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = PythonGrammarParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(PythonGrammarParser.ID)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 99
                self.match(PythonGrammarParser.T__17)
                self.state = 100
                self.match(PythonGrammarParser.ID)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(PythonGrammarParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(PythonGrammarParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(PythonGrammarParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PythonGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(PythonGrammarParser.NEWLINE)
                self.state = 107
                self.match(PythonGrammarParser.INDENT)
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 108
                    self.statement()
                    self.state = 111 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7934976) != 0)):
                        break

                self.state = 113
                self.match(PythonGrammarParser.DEDENT)
                pass
            elif token in [10, 12, 16, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.statement()
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


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PythonGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = PythonGrammarParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(PythonGrammarParser.T__18)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 119
                self.expression(0)


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
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         





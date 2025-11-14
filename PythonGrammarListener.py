# Generated from PythonGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonGrammarParser import PythonGrammarParser
else:
    from PythonGrammarParser import PythonGrammarParser

# This class defines a complete listener for a parse tree produced by PythonGrammarParser.
class PythonGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by PythonGrammarParser#program.
    def enterProgram(self, ctx:PythonGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#program.
    def exitProgram(self, ctx:PythonGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#statement.
    def enterStatement(self, ctx:PythonGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#statement.
    def exitStatement(self, ctx:PythonGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#assignment.
    def enterAssignment(self, ctx:PythonGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#assignment.
    def exitAssignment(self, ctx:PythonGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#expression.
    def enterExpression(self, ctx:PythonGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#expression.
    def exitExpression(self, ctx:PythonGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#if_statement.
    def enterIf_statement(self, ctx:PythonGrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#if_statement.
    def exitIf_statement(self, ctx:PythonGrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#while_statement.
    def enterWhile_statement(self, ctx:PythonGrammarParser.While_statementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#while_statement.
    def exitWhile_statement(self, ctx:PythonGrammarParser.While_statementContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#function_def.
    def enterFunction_def(self, ctx:PythonGrammarParser.Function_defContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#function_def.
    def exitFunction_def(self, ctx:PythonGrammarParser.Function_defContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#parameters.
    def enterParameters(self, ctx:PythonGrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#parameters.
    def exitParameters(self, ctx:PythonGrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#block.
    def enterBlock(self, ctx:PythonGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#block.
    def exitBlock(self, ctx:PythonGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#return_statement.
    def enterReturn_statement(self, ctx:PythonGrammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#return_statement.
    def exitReturn_statement(self, ctx:PythonGrammarParser.Return_statementContext):
        pass



del PythonGrammarParser
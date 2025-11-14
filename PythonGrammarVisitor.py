# Generated from PythonGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonGrammarParser import PythonGrammarParser
else:
    from PythonGrammarParser import PythonGrammarParser

# This class defines a complete generic visitor for a parse tree produced by PythonGrammarParser.

class PythonGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonGrammarParser#program.
    def visitProgram(self, ctx:PythonGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#statement.
    def visitStatement(self, ctx:PythonGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#assignment.
    def visitAssignment(self, ctx:PythonGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#expression.
    def visitExpression(self, ctx:PythonGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#if_statement.
    def visitIf_statement(self, ctx:PythonGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#while_statement.
    def visitWhile_statement(self, ctx:PythonGrammarParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#function_def.
    def visitFunction_def(self, ctx:PythonGrammarParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#parameters.
    def visitParameters(self, ctx:PythonGrammarParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#block.
    def visitBlock(self, ctx:PythonGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonGrammarParser#return_statement.
    def visitReturn_statement(self, ctx:PythonGrammarParser.Return_statementContext):
        return self.visitChildren(ctx)



del PythonGrammarParser
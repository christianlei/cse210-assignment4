from antlr4 import *
from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool

if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser


# This class defines a complete generic visitor for a parse tree produced by WhileParser.

class WhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileParser#compileUnit.
    def visitCompileUnit(self, ctx: WhileParser.CompileUnitContext):
        return self.visit(ctx.semi_stat())

    # Visit a parse tree produced by WhileParser#INFIX.
    def visitINFIX(self, ctx: WhileParser.INFIXContext):
        node = BinaryOp()
        if ctx.OP_ADD():
            node.op = '+'
        elif ctx.OP_SUB():
            node.op = '-'
        elif ctx.OP_MUL():
            node.op = '*'
        elif ctx.OP_ASGN():
            node.op = ':='
        elif ctx.OP_EQ():
            node.op = '='
        elif ctx.OP_LESS():
            node.op = '<'
        elif ctx.OP_AND():
            node.op = '∧'
        elif ctx.OP_OR():
            node.op = '∨'
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node

    # Visit a parse tree produced by WhileParser#PARENGRP.
    def visitPARENGRP(self, ctx: WhileParser.PARENGRPContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by WhileParser#INT.
    def visitINT(self, ctx: WhileParser.INTContext):
        return Int(value=int(str(ctx.NUMBER())))

    # Visit a parse tree produced by WhileParser#VAL.
    def visitVAL(self, ctx: WhileParser.VALContext):
        if ctx.VAR():
            return Var(value=(str(ctx.VAR())))

    # Visit a parse tree produced by WhileParser#BOOL.
    def visitBOOL(self, ctx: WhileParser.BOOLContext):
        if ctx.TRUE():
            return Bool(value=(bool(True)))
        elif ctx.FALSE():
            return Bool(value=(bool(False)))

    # Visit a parse tree produced by WhileParser#UNARY.
    def visitUNARY(self, ctx: WhileParser.UNARYContext):
        if ctx.OP_ADD():
            return self.visit(ctx.expr())
        elif ctx.OP_SUB():
            return NegInt(node=self.visit(ctx.expr()))

    # Visit a parse tree produced by WhileParser#PASS.
    def visitPASS(self, ctx: WhileParser.PASSContext):
        return

    # Visit a parse tree produced by WhileParser#stat.
    def visitStat(self, ctx: WhileParser.StatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by WhileParser#if_stat.
    def visitIf_stat(self, ctx: WhileParser.If_statContext):
        node = Expression()
        node.conditional = self.visit(ctx.conditional)
        node.true = self.visit(ctx.true)
        node.false = self.visit(ctx.false)
        node.method = 'if'
        return node

    # Visit a parse tree produced by WhileParser#stat.
    def visitSemi_stat(self, ctx:WhileParser.StatContext):
        list_of_stat = ctx.stat()
        if len(list_of_stat) == 1:
            return self.visit(list_of_stat.pop(0))

        root_node = MultiExpression()
        list_of_stat = ctx.stat()
        root_node.first = self.visit(list_of_stat.pop(0))
        node = root_node
        while len(list_of_stat) > 0:
            next_node = MultiExpression()
            next_node.first = self.visit(list_of_stat.pop(0))
            node.next = next_node
            node = next_node
        return root_node

    # Visit a parse tree produced by WhileParser#UNARYBOOL.
    def visitUNARYBOOL(self, ctx: WhileParser.UNARYBOOLContext):
        if ctx.OP_NOT():
            return NotOp(node=self.visit(ctx.expr()))

    # Visit a parse tree produced by WhileParser#PARENWHILEBLOCK.
    def visitPARENWHILEBLOCK(self, ctx: WhileParser.PARENWHILEBLOCKContext):
        node = Expression()
        node.conditional = self.visit(ctx.conditional)
        node.true = self.visit(ctx.inner)
        node.method = 'while'
        return node

    # Visit a parse tree produced by WhileParser#NOPAREN.
    def visitNOPAREN(self, ctx: WhileParser.NOPARENContext):
        node = Expression()
        node.conditional = self.visit(ctx.conditional)
        node.true = self.visit(ctx.inner_no_brace)
        node.method = 'while'
        return node


del WhileParser

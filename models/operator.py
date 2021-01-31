from ast import AST


class BinaryOp(AST):
    def __init__(self, op=None, left=None, right=None):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return str(self.left) + " " + str(self.op) + " " + str(self.right)

class NotOp(AST):
    def __init__(self, node):
        self.node = node

    def __str__(self):
        return str(self.node)


class Expression(AST):
    def __init__(self, conditional=None, true=None, false=None, method=None):
        self.true = true
        self.conditional = conditional
        self.false = false
        self.method = method

    def __str__(self):
        if self.method == 'if':
            return "if " + str(self.conditional) \
                   + " then { " + str(self.true) + " } else { " \
                   + str(self.false) + " }"
        if self.method == 'while':
            return "while " + " (" + str(self.conditional) + ") " \
                   + " do { " + str(self.true) + " }"
        return


class MultiExpression(AST):
    def __init__(self, first=None, next=None):
        self.first = first
        self.next = next

    def __str__(self):
        return

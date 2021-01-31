from ast import AST


class Int(AST):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class NegInt(AST):
    def __init__(self, node):
        self.value = -1 * node.value

    def __str__(self):
        return str(self.value)


class Var(AST):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Bool(AST):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
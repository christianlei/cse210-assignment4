from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.d = {}
        self.empty_var = 0

    def check_in_dict(self, var):
        if var in self.d:
            return self.d[var]
        return self.empty_var

    def return_int_value(self, item):
        if isinstance(item, int):
            return item
        if isinstance(item, str):
            return self.check_in_dict(item)

    def evaluate_if_expression(self, item):
        if self.eval(item.conditional):
            return self.eval(item.true)
        else:
            if item.false is not None:
                return self.eval(item.false)
            else:
                return None

    def eval(self, item):
        if isinstance(item, MultiExpression):
            self.eval(item.first)
            if item.next is not None:
                self.eval(item.next)

        if isinstance(item, Expression):
            if item.method == 'if':
                return self.evaluate_if_expression(item)
            elif item.method == 'while':
                while self.eval(item.conditional):
                    self.eval(item.true)

        if isinstance(item, NotOp):
            return not self.eval(item.node)

        if isinstance(item, BinaryOp):
            if item.op == ':=':
                self.d[self.eval(item.left)] = self.return_int_value(self.eval(item.right))

            left_item = self.eval(item.left)
            right_item = self.eval(item.right)
            if item.op == '=':
                return self.return_int_value(left_item) == self.return_int_value(right_item)
            if item.op == '<':
                return self.return_int_value(left_item) < self.return_int_value(right_item)
            if item.op == '-':
                return self.return_int_value(left_item) - self.return_int_value(right_item)
            if item.op == '*':
                return self.return_int_value(left_item) * self.return_int_value(right_item)
            if item.op == '+':
                return self.return_int_value(left_item) + self.return_int_value(right_item)
            if item.op == '∧':
                return self.return_int_value(left_item) and self.return_int_value(right_item)
            if item.op == '∨':
                return self.return_int_value(left_item) or self.return_int_value(right_item)

        if isinstance(item, Int) or isinstance(item, NegInt):
            return item.value
        elif isinstance(item, Var):
            return item.value
        elif isinstance(item, Bool):
            return item.value
        return

    def dictionary_to_result(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_list = sorted(return_list)
        return_string = ", ".join(return_list)
        final_result = '{' + return_string + '}'
        print(final_result)

from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.d = {}
        self.empty_var = 0
        self.output_string = ""
        self.first_command = False

    def print_result(self):
        print(self.output_string)

    def add_to_output_string(self, string):
        if not self.first_command:
            self.first_command = True
            return
        self.output_string += string

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
            self.add_to_output_string(str(item.true))
            return self.eval(item.true)
        else:
            if item.false is not None:
                self.add_to_output_string(str(item.false))
                return self.eval(item.false)
            else:
                return None

    def eval(self, item):
        if isinstance(item, MultiExpression):
            self.eval(item.first)
            if item.next is not None:
                self.eval(item.next)

        if isinstance(item, Expression):
            self.add_to_output_string(str(Expression))
            if item.method == 'if':
                return self.evaluate_if_expression(item)
            elif item.method == 'while':
                while self.eval(item.conditional):
                    self.eval(item.true)
                if not self.eval(item.conditional):
                    self.add_to_output_string("⇒ skip")

        if isinstance(item, NotOp):
            return not self.eval(item.node)

        if isinstance(item, BinaryOp):
            response = None
            left_item = self.eval(item.left)
            right_item = self.eval(item.right)
            if item.op == ':=':
                if self.first_command:
                    self.dictionary_to_result()
                if self.output_string:
                    self.output_string += '\n'
                self.d[left_item] = self.return_int_value(right_item)
                self.first_command = True
            if item.op == '=':
                response = self.return_int_value(left_item) == self.return_int_value(right_item)
            if item.op == '<':
                response = self.return_int_value(left_item) < self.return_int_value(right_item)
            if item.op == '-':
                response = self.return_int_value(left_item) - self.return_int_value(right_item)
            if item.op == '*':
                response = self.return_int_value(left_item) * self.return_int_value(right_item)
            if item.op == '+':
                response = self.return_int_value(left_item) + self.return_int_value(right_item)
            if item.op == '∧':
                response = self.return_int_value(left_item) and self.return_int_value(right_item)
            if item.op == '∨':
                response = self.return_int_value(left_item) or self.return_int_value(right_item)
            self.add_to_output_string("⇒ skip")
            return response

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
        # if not len(self.d.items()):
        #     return
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_list = sorted(return_list)
        return_string = ", ".join(return_list)
        final_result = '{' + return_string + '}'
        if self.output_string:
            self.output_string += ', ' + final_result

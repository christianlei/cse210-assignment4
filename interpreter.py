from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.d = {}
        self.empty_var = 0
        self.output_string = ""
        self.first_command = False
        self.new_line = True

    def print_result(self):
        print(self.output_string)

    def add_to_output_string(self, string):
        if self.new_line:
            self.output_string += "⇒ "
            self.new_line = False
        if not self.first_command:
            self.first_command = True
            return False
        self.output_string += string
        return True

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

    def evaluate_while_loop(self, item):
        if self.eval(item.conditional):
            self.add_to_output_string(str(item.true))
            self.eval(item.true)
            self.add_to_output_string(str(item))
            return self.eval(item)
        else:
            self.add_to_output_string("skip")

    def eval(self, item):
        if isinstance(item, MultiExpression):
            self.eval(item.first)
            if item.next is not None:
                self.eval(item.next)

        if isinstance(item, Expression):
            self.add_to_output_string(str(item))
            if item.method == 'if':
                return self.evaluate_if_expression(item)
            elif item.method == 'while':
                return self.evaluate_while_loop(item)

        if isinstance(item, NotOp):
            return not self.eval(item.node)

        if isinstance(item, BinaryOp):
            left_item = self.eval(item.left)
            right_item = self.eval(item.right)
            if item.op == ':=':
                if self.add_to_output_string(str(item)) and self.first_command:
                    self.dictionary_to_result()
                    self.output_string += '\n'
                    self.new_line = True
                self.add_to_output_string("skip")
                self.d[left_item] = self.return_int_value(right_item)
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
        # if not len(self.d.items()):
        #     return
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_list = sorted(return_list)
        return_string = ", ".join(return_list)
        final_result = '{' + return_string + '}'
        if self.output_string:
            self.output_string += ', ' + final_result

from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.d = {}
        self.empty_var = 0
        self.output_string = ""
        self.first_command = True
        self.new_line = True
        self.while_exp = False
        self.multi_exp = False

    def print_result(self):
        print(self.output_string)

    def add_to_output_string(self, string):
        if self.new_line:
            self.output_string += "⇒ "
            self.new_line = False
        if self.first_command:
            self.first_command = False
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
        first_command = self.first_command
        self.add_to_output_string(str(item))
        if not first_command:
            self.output_string += self.dictionary_to_result()
            self.output_string += '\n'
            self.new_line = True
            self.add_to_output_string(str(item))
            self.output_string += self.dictionary_to_result()
            self.output_string += '\n'
            self.new_line = True
        if self.eval(item.conditional):
            if not first_command:
                self.add_to_output_string(str(item.true))
                self.output_string += self.dictionary_to_result()
                self.output_string += '\n'
                self.new_line = True
            return self.eval(item.true)
        if item.false is not None:
            return self.eval(item.false)
        return None

    def evaluate_while_loop(self, item, true_run=False):
        self.add_to_output_string(str(item))
        if self.eval(item.conditional):
            self.while_exp = True
            dict_state_before = self.dictionary_to_result()
            self.eval(item.true)
            self.add_to_output_string("; " + str(item))
            self.output_string += dict_state_before
            self.output_string += '\n'
            self.new_line = True
            self.add_to_output_string("skip; ")
            self.add_to_output_string(str(item))
            self.output_string += self.dictionary_to_result()
            self.output_string += '\n'
            self.new_line = True
            self.while_exp = False
            return self.evaluate_while_loop(item, True)
        else:
            if true_run:
                self.output_string += self.dictionary_to_result()
                self.output_string += '\n'
                self.new_line = True
            self.add_to_output_string("skip")
            self.output_string += self.dictionary_to_result()
            self.output_string += '\n'
            self.new_line = True

    def handle_multi_expression(self, item):
        if item.next is not None:
            self.multi_exp = True
        self.eval(item.first)
        if item.next is not None:
            self.output_string += "; "
            if item.brackets:
                dictionary_before = self.dictionary_to_result()
                self.add_to_output_string(str(item.next))
                self.output_string += dictionary_before
                self.output_string += '\n'
                self.new_line = True
                self.add_to_output_string(str(item.next))
                self.output_string += self.dictionary_to_result()
                self.output_string += '\n'
                self.new_line = True
            self.eval(item.next)
        if item.next is None and self.multi_exp:
            self.output_string += self.dictionary_to_result()

    def handle_assignment_op(self, item):
        left_item = self.eval(item.left)
        right_item = self.eval(item.right)
        if self.first_command or not self.multi_exp:
            self.add_to_output_string(str(item))
        if not self.first_command and not self.while_exp and not self.multi_exp \
                and self.output_string != "⇒ ":
            self.output_string += self.dictionary_to_result()
            self.output_string += '\n'
            self.new_line = True
        self.d[left_item] = self.return_int_value(right_item)
        if not self.while_exp and not self.multi_exp:
            self.add_to_output_string("skip")
            self.output_string += self.dictionary_to_result()
        if self.multi_exp:
            self.add_to_output_string("skip")

    def eval(self, item):
        if isinstance(item, MultiExpression):
            self.handle_multi_expression(item)

        if isinstance(item, Expression):
            if item.method == 'if':
                return self.evaluate_if_expression(item)
            elif item.method == 'while':
                return self.evaluate_while_loop(item)

        if isinstance(item, NotOp):
            return not self.eval(item.node)

        if isinstance(item, BinaryOp):
            if item.op == ':=':
                self.handle_assignment_op(item)
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
        return ', {' + return_string + '}'

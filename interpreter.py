from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.store = {}
        self.empty_var = 0
        self.output_string = ""
        self.first_command = True
        self.new_line = True
        self.while_exp = False
        self.multi_exp = False
        self.first_command_printed = False
        self.error_value = -9999

    def print_result(self):
        print(self.output_string)

    def adding_dictionary_to_end(self):
        self.output_string += self.dictionary_to_string()
        self.output_string += '\n'
        self.new_line = True

    def adding_dictionary_before_to_end(self, dictionary_before):
        self.output_string += dictionary_before
        self.output_string += '\n'
        self.new_line = True

    def dictionary_to_string(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.store.items():
            return_list.append(string_format.format(key, value))
        return_list = sorted(return_list)
        return_string = ", ".join(return_list)
        return ', {' + return_string + '}'

    def add_to_output_string(self, string):
        if self.new_line:
            self.output_string += "⇒ "
            self.new_line = False
        if self.first_command:
            self.first_command = False
            return
        self.first_command_printed = True
        self.output_string += string

    def check_in_dict(self, var):
        if var in self.store:
            return self.store[var]
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
            self.adding_dictionary_to_end()
            self.add_to_output_string(str(item))
            self.adding_dictionary_to_end()
        if self.eval(item.conditional):
            if not first_command:
                self.add_to_output_string(str(item.true))
                self.adding_dictionary_to_end()
            return self.eval(item.true)
        if item.false is not None:
            return self.eval(item.false)
        return None

    def evaluate_while_loop(self, item, true_run=False):
        self.add_to_output_string(str(item))
        conditional_bool = self.eval(item.conditional)
        if conditional_bool and self.first_command_printed:
            self.adding_dictionary_to_end()

        if conditional_bool:
            self.while_exp = True
            dictionary_before = self.dictionary_to_string()
            # self.adding_dictionary_before_to_end(dictionary_before)
            self.eval(item.true)
            self.add_to_output_string("; " + str(item))
            self.adding_dictionary_before_to_end(dictionary_before)
            self.add_to_output_string("skip; ")
            self.add_to_output_string(str(item))
            self.adding_dictionary_to_end()
            self.while_exp = False
            return self.evaluate_while_loop(item, True)
        if true_run:
            self.adding_dictionary_to_end()
        self.add_to_output_string("skip")
        self.adding_dictionary_to_end()

    def handle_multi_expression(self, item):
        if item.next is not None:
            self.multi_exp = True
        self.eval(item.first)
        if item.next is not None:
            self.output_string += "; "
            if item.brackets:
                dictionary_before = self.dictionary_to_string()
                self.add_to_output_string(str(item.next))
                self.adding_dictionary_before_to_end(dictionary_before)
                self.add_to_output_string(str(item.next))
                self.adding_dictionary_to_end()
            self.eval(item.next)
        if item.next is None and self.multi_exp:
            self.output_string += self.dictionary_to_string()

    def handle_assignment_op(self, item):
        left_item = self.eval(item.left)
        right_item = self.eval(item.right)
        if self.first_command or not self.multi_exp:
            self.add_to_output_string(str(item))
        if not self.first_command and not self.while_exp and not self.multi_exp \
                and self.output_string != "⇒ ":
            self.adding_dictionary_to_end()
        self.store[left_item] = self.return_int_value(right_item)
        if not self.while_exp and not self.multi_exp:
            self.add_to_output_string("skip")
            self.output_string += self.dictionary_to_string()
        if self.multi_exp:
            self.add_to_output_string("skip")

    def eval(self, item):
        # print("item passed to eval: ", str(type(item)) + " " + str(item))
        # print(self.store)
        if self.error_value in self.store:
            return
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

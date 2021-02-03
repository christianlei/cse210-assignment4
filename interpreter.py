from models.operator import BinaryOp, Expression, MultiExpression, NotOp
from models.item import Int, NegInt, Var, Bool, Dictionary, Skip


class Interpreter:

    def __init__(self):
        self.store = {}
        self.empty_var = 0
        self.output_string = ""
        self.store_before = None
        self.new_line = True
        self.first_command = True
        self.deque = []
        self.deque_first = True
        self.num_of_multi_run = 0
        self.num_of_evals = 0

    def add_remainder_of_deque_to_store(self):
        while self.deque:
            deq_item = self.deque.pop(0)
            if not self.deque:
                self.output_string += str(deq_item)
            else:
                if not isinstance(self.deque[0], Dictionary) and not isinstance(deq_item, Dictionary):
                    self.output_string += str(deq_item) + "; "
                else:
                    self.output_string += str(deq_item)
                if isinstance(deq_item, Dictionary):
                    self.output_string += "⇒ "

    def print_result(self):
        self.add_remainder_of_deque_to_store()
        print(self.output_string.rstrip())

    def add_to_output_deque(self, item, dictionary=None):
        if not self.deque and self.output_string != "⇒ ":
            self.output_string += "⇒ "
        if not self.deque_first:
            self.deque.append(item)
            if dictionary is not None:
                self.deque.append(dictionary)
        else:
            self.deque_first = False

    def check_in_dict(self, var):
        if var in self.store:
            return self.store[var]
        return self.empty_var

    def dictionary_to_string(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.store.items():
            return_list.append(string_format.format(key, value))
        return_list = sorted(return_list)
        return_string = ", ".join(return_list)
        return ', {' + return_string + '}'

    def return_int_value(self, item):
        if isinstance(item, int):
            return item
        if isinstance(item, str):
            return self.check_in_dict(item)

    def evaluate_if_expression(self, item):
        self.add_to_output_deque(str(item), Dictionary(self.dictionary_to_string()))
        if self.eval(item.conditional):
            return self.eval(item.true)
        else:
            if item.false is not None:
                return self.eval(item.false)
            else:
                return None

    def evaluate_while_loop(self, item):
        self.num_of_evals += 1
        conditional = self.eval(item.conditional)
        self.add_to_output_deque(str(item), Dictionary(self.dictionary_to_string()))
        self.add_remainder_of_deque_to_store()  # adding new step to output, might need to adjust if line above not run
        if self.num_of_evals > 3333:
            self.add_to_output_deque(str(item.true) + "; " + str(item), Dictionary(self.dictionary_to_string()))
            return
        if conditional:
            new_deque = []
            self.eval(item.true)
            deq_len = len(self.deque)
            for i in range(deq_len):
                deq_item = self.deque.pop(0)
                if not self.deque:  # Deque Empty ( add dictionary)
                    new_deque.append(deq_item)
                elif isinstance(self.deque[0], Dictionary) and i == (deq_len - 1):
                    new_deque.append(deq_item)  # Final Item, add skip after
                    new_deque.append(Skip())
                elif isinstance(self.deque[0], Dictionary):  # Not a final dictionary, add while behind to do
                    new_deque.append(deq_item)
                    new_deque.append(str(item))
                else:
                    new_deque.append(deq_item)
            self.deque = new_deque
            self.add_remainder_of_deque_to_store()
            self.evaluate_while_loop(item)

        else:
            self.add_to_output_deque(Skip(), Dictionary(self.dictionary_to_string()))

    def evaluate_assignment_op(self, item):
        self.add_to_output_deque(str(item), Dictionary(self.dictionary_to_string()))
        self.store[self.eval(item.left)] = self.return_int_value(self.eval(item.right))
        self.add_to_output_deque(Skip(), Dictionary(self.dictionary_to_string()))

    def evaluate_multi_expressions(self, item):
        self.eval(item.first)
        if item.next is not None:
            if len(self.deque) == 10:
                self.deque.insert(-3, str(item.next))
                self.deque.insert(-1, str(item.next))
            elif not len(self.deque) == 2:
                self.deque.insert(1, str(item.next))
                self.deque.insert(-1, str(item.next))
            else:
                self.deque.insert(1, str(item.next))
        if not self.num_of_multi_run:
            self.add_remainder_of_deque_to_store()
        self.num_of_multi_run += 1
        if item.next is not None:
            self.eval(item.next)

    def eval(self, item):
        if isinstance(item, Int) or isinstance(item, NegInt):
            return item.value
        elif isinstance(item, Var):
            return item.value
        elif isinstance(item, Bool):
            return item.value

        if isinstance(item, NotOp):
            return not self.eval(item.node)

        if isinstance(item, BinaryOp):
            if item.op == ':=':
                return self.evaluate_assignment_op(item)

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

        if isinstance(item, MultiExpression):
            self.evaluate_multi_expressions(item)

        if isinstance(item, Expression):
            if item.method == 'if':
                return self.evaluate_if_expression(item)
            elif item.method == 'while':
                return self.evaluate_while_loop(item)

        return

"""
This module decouples the logic for the day 2 aoc2019 into utility functions and entities
"""


def add(args):
    """Function adds the passed numbers together"""
    sum = 0  # initialize sum
    for x in args:
        sum += x
    return sum


def multiply(args):
    """Function multiples the passed numbers together"""
    product = 1
    # multiply the passed values
    for x in args:
        product *= x
    return product


def stop():
    """Simple utility function that raises Done exception to signal completion"""
    raise Done
    pass


class IntCode:
    DEF_INPUT = 1
    """Class to define attributes and behavior for an 'int code' collection"""
    def __init__(self, args):
        """Simple ctor"""
        self.list = args
        self.codes = {1: self.add_opp, 2: self.multiply_opp, 99: stop}  # dynamic dispatch function calls
        self.index = 0
        self.isDone = False
        self.output_codes = []  # a list to store the resulting output codes

    def visit(self):
        """Visits a block of 4 int codes and does an operation"""
        # special case - done
        if self.isDone:
            return

        code = self.list[self.index]
        try:
            #target = self.list[self.index + 3]
            #terms = [self.list[self.list[self.index + 1]], 0]
            #terms[1] = self.list[self.list[self.index + 2]]
            #self.list[target] = self.codes[code](terms)
            self.codes[code]()
        # out of bounds
        except (IndexError, TypeError):
            #try:
            #    self.list[target] = self.codes[code]()
            #except TypeError:
            #    # invalid initial values
            #    stop()
            pass

    def get_value(self, offset):
        """
        Utility method that returns either the positional indexed value or
        immediate literal value - depending on instruction opp code
        """
        code = f'{self.list[self.index]:05}'
        param = self.list[self.index + offset]
        # parameter mode is 1 - immediate mode
        if '1' == code[-2 - offset]:
            return param
        # parameter mode is 0 - position mode
        else:
            return self.list[param]

    def visit_next(self):
        """Visits the next block of int codes"""
        try:
            self.visit()
        except Done:
            # print('Hit code 99 - done.')
            self.isDone = True
        except KeyError:
            print('An error has occurred - wrong opp code')

        self.index += 4

    def visit_all(self):
        """Iterates through all int code blocks"""
        while not self.isDone:
            self.visit_next()

    def input_opp(self):
        """This operation takes an index and saves the "input" at the index parameter"""
        param = self.list[self.index + 1]
        self.list[param] = self.DEF_INPUT

    def output_opp(self):
        """
        This operations prints either the passed value or the value at the
        passed index. Instruction 4, 50 indicates instruction # 4 (this instruction) and 0
        for the parameter mode - ie position mode. It outputs the value stored at index 50.
        """
        # "output" the output code with the get_value result - parameter offset of 1
        self.output_codes.append(self.get_value(1))

    def add_opp(self):
        """
        This operation adds two numbers - passing the appropriate terms to
        the add function"""
        target = self.list[self.index + 3]
        terms = [self.get_value(1), self.get_value(2)]
        self.list[target] = add(terms)

    def multiply_opp(self):
        """
        This operation multiples two numbers - passing the appropriate terms
        to the multiply function
        """

        target = self.list[self.index + 3]
        terms = [self.get_value(1), self.get_value(2)]
        # terms[1] = self.list[self.get_value(2)]
        self.list[target] = multiply(terms)


class Done(Exception):
    """Simple custom exception"""
    pass


def brute_force(instruction_list, target_value):
    """
    This method finds binary tuple of values for a specific target and
    computes the evaluated result
    """
    value_one = 0
    value_two = 0
    # iterate through possibilities
    for i in range(target_value):
        input_clone = instruction_list[:]
        input_clone[1] = i
        input_clone[2] = value_two
        test_run = IntCode(input_clone)
        test_run.visit_all()
        # test value at index 0
        if target_value < test_run.list[0]:
            value_one = i - 1
            break
        if target_value == test_run.list[0]:
            value_one = i
            return 100 * value_one + value_two

    for j in range(target_value):
        input_clone = instruction_list[:]
        input_clone[1] = value_one
        input_clone[2] = j
        test_run = IntCode(input_clone)
        test_run.visit_all()
        # test value at index 0
        if target_value == test_run.list[0]:
            value_two = j
            return 100 * value_one + value_two

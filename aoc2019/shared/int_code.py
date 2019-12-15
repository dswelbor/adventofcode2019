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
    JUMP_TRUE_CODE = 5
    JUMP_FALSE_CODE = 6
    JUMP_OFFSET = 3
    """Class to define attributes and behavior for an 'int code' collection"""
    def __init__(self, args):
        """Simple ctor"""
        self.init_input = self.DEF_INPUT
        self.list = args
        # dynamic dispatch function calls
        self.codes = {1: self.add_opp,
                      2: self.multiply_opp,
                      3: self.input_opp,
                      4: self.output_opp,
                      5: self.jump_true_opp,
                      6: self.jump_false_opp,
                      7: self.less_opp,
                      8: self.equals_opp,
                      99: stop}
        # dynamic index increment values
        self.increment_value = {1: 4,
                                2: 4,
                                3: 2,
                                4: 2,
                                self.JUMP_TRUE_CODE: self.JUMP_OFFSET,
                                self.JUMP_FALSE_CODE: self.JUMP_OFFSET,
                                7: 4,
                                8: 4,
                                99: 4}
        self.index = 0
        self.isDone = False
        self.output_codes = []  # a list to store the resulting output codes

    def run(self, init_input):
        """
        This method initializes run with the passed input, then proceeds to
        process the object's instructions.
        """
        self.init_input = init_input
        self.visit_all()

    def visit(self):
        """Visits a block of 4 int codes and does an operation"""
        # special case - done
        if self.isDone:
            return

        code = self.get_instruction()
        try:
            # dynamic dispatch based on instruction code
            self.codes[code]()
        # out of bounds
        except (IndexError, TypeError):
            # do nothing exception handler
            pass

    def get_value(self, offset):
        """
        Utility method that returns either the positional indexed value or
        immediate literal value - depending on instruction opp code
        """
        # code = f'{self.list[self.index]:05}'
        code = '{0:05}'.format(self.list[self.index])
        param = self.list[self.index + offset]
        # parameter mode is 1 - immediate mode
        if '1' == code[-2 - offset]:
            return param
        # parameter mode is 0 - position mode
        else:
            return self.list[param]

    def get_instruction(self):
        code = str(self.list[self.index])[-2:]
        return int(code)

    def visit_next(self):
        """Visits the next block of int codes"""
        code = self.get_instruction()  # save instruction code for current iteration
        try:
            self.visit()
        except Done:
            # print('Hit code 99 - done.')
            self.isDone = True
        except KeyError:
            print('An error has occurred - wrong opp code')

        # dynamically increment the instruction pointer
        self.index += self.increment_value[code]

    def visit_all(self):
        """Iterates through all int code blocks"""
        while not self.isDone:
            self.visit_next()

    def input_opp(self):
        """
        Instruction # 3: This operation takes an index and saves the "input" at
        the index parameter
        """
        param = self.list[self.index + 1]
        self.list[param] = self.init_input

    def output_opp(self):
        """
        Instruction # 4: This operations prints either the passed value or the value at the
        passed index. Instruction 4, 50 indicates instruction # 4 (this instruction) and 0
        for the parameter mode - ie position mode. It outputs the value stored at index 50.
        """
        # "output" the output code with the get_value result - parameter offset of 1
        self.output_codes.append(self.get_value(1))

    def add_opp(self):
        """
        Instruction # 1: This operation adds two numbers - passing the appropriate
        terms to the add function.
        """
        target = self.list[self.index + 3]
        terms = [self.get_value(1), self.get_value(2)]
        self.list[target] = add(terms)

    def multiply_opp(self):
        """
        Instruction # 2: This operation multiples two numbers - passing the appropriate terms
        to the multiply function
        """

        target = self.list[self.index + 3]
        terms = [self.get_value(1), self.get_value(2)]
        # terms[1] = self.list[self.get_value(2)]
        self.list[target] = multiply(terms)

    def jump_true_opp(self):
        """
        Instruction # 5: if the first parameter is non-zero, it sets the instruction pointer
        to the value from the second parameter. Otherwise, it does nothing.
        """
        param_one = self.get_value(1)
        param_two = self.get_value(2)

        # first param is non-zero - jump to instruction at 2nd param
        if param_one is not 0:
            self.index = param_two
            self.increment_value[self.JUMP_TRUE_CODE] = 0  # index ptr moved already

        # first param is zero (false) - do nothing
        else:
            # don't modify index ptr
            # re-set increment value to appropriate offset
            self.increment_value[self.JUMP_TRUE_CODE] = self.JUMP_OFFSET

    def jump_false_opp(self):
        """
        Instruction # 6: if the first parameter is zero, it sets the instruction
        pointer to the value from the second parameter. Otherwise, it does nothing.
        """
        param_one = self.get_value(1)
        param_two = self.get_value(2)

        # first param is zero (false) - jump to instruction at 2nd param
        if param_one is 0:
            self.index = param_two
            self.increment_value[self.JUMP_FALSE_CODE] = 0  # index ptr moved already

        # first param is non-zero (true) - do nothing
        else:
            # don't modify index ptr
            # re-set increment value to appropriate offset
            self.increment_value[self.JUMP_FALSE_CODE] = self.JUMP_OFFSET

    def less_opp(self):
        """
        Instruction #7: if the first parameter is less than the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it
        stores 0.
        """
        # get three params
        param_one = self.get_value(1)
        param_two = self.get_value(2)
        target = self.get_value(3)
        # param 1 less than param 2
        if param_one < param_two:
            self.list[target] = 1
        # param 1 is not less than param 2
        else:
            self.list[target] = 0

    def equals_opp(self):
        """
        Instruction #8: if the first parameter is equal to the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it
        stores 0.
        """
        # get three params
        param_one = self.get_value(1)
        param_two = self.get_value(2)
        target = self.get_value(3)
        # param1 == param2
        if param_one is param_two:
            self.list[target] = 1
        # param 1 != param 2
        else:
            self.list[target] = 0


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

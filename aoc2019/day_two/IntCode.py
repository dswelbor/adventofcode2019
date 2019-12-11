
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
    """Class to define attributes and behavior for an 'int code' collection"""
    def __init__(self, args):
        """Simple ctor"""
        self.list = args
        self.codes = {1: add, 2: multiply, 99: stop}
        self.index = 0

    def visit(self):
        """Visits a block of 4 int codes and does an operation"""
        code = self.list[self.index]
        target = self.list[self.index + 3]
        try:
            # list.insert(target, self.codes[code](self.list[index + 1: index + 3]))
            self.list[target] = self.codes[code](self.list[self.index + 1: self.index + 3])
        # out of bounds
        except IndexError:
            self.list[target] = self.codes[code]()

    def visit_next(self):
        """Visits the next block of int codes"""
        try:
            self.visit()
        except Done:
            print('Hit code 99 - done.')
        except KeyError:
            print('An error has occurred - wrong opp code')

        self.index += 4

    def visit_all(self):
        """Iterates through all int code blocks"""
        while self.index < len(self.list):
            self.visit_next()


class Done(Exception):
    """Simple custom exception"""
    pass

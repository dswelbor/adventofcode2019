def valid(input):
    permutation = str(input)
    # six digit number
    if not isinstance(input, int) or len(str(input)) != 6:
        # not a size digit number
        return False

    # increasing (next digit is > or ==)
    try:
        prev = permutation[0]
        for digit in permutation[1:]:
            # not increasing
            if digit < prev:
                return False
            prev = digit

        # at lease 2 adjacent digits are the same
        prev = permutation[0]
        for digit in permutation[1:]:
            # one adjacent match pair
            if digit == prev:
                return True
        # Not matching adjacent digits - invalid
        return False

    except IndexError:
        print('Empty input - invalid')
        raise TypeError


class CrackIt:
    """
    This is a class that stores values for Secure Container password ranges
    and provides behavior to iteratively list valid potential passwords.
    """

    def __init__(self, start, end):
        """Simple initialization method for object attributes"""
        self.range_start = start
        self.range_end = end
        self.valid_candidates = []  # a list of valid password candidates

    def get_valid_permutations(self):
        """Utility method to generate list of valid password candidates"""
        # iterate through possibilities - inclusive range
        for permutation in range(self.range_start, self.range_end + 1):
            if valid(permutation):
                self.valid_candidates.append(permutation)

        # list of valid candidates generated
        return self.valid_candidates

    def get_num_valid_permutations(self):
        """Simple utility method to return the number of valid possibilities"""
        return len(self.get_valid_permutations())

def valid(candidate):
    """Utility function that returns whether a pass permutation is valid"""
    permutation = str(candidate)
    # six digit number
    if not isinstance(candidate, int) or len(str(candidate)) != 6:
        # not a size digit number
        return False

    # increasing (next digit is > or ==)
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
        prev = digit
    # Not matching adjacent digits - invalid
    return False


def valid_refined(candidate):
    """
    Utility function that determines if a passed permutation is valid.
    Specifically, there exists one and only one "pair" of matching digits.
    """
    permutation = str(candidate)
    for char in permutation[::-1]:
        if 2 == permutation.count(char):
            return True
    # didn't find a true condition
    return False


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
        self.valid_candidates_refined = []  # a list of refined valid password candidates

    def get_valid_permutations(self):
        """Utility method to generate list of valid password candidates"""
        # iterate through possibilities - inclusive range
        for permutation in range(self.range_start, self.range_end + 1):
            if valid(permutation):
                self.valid_candidates.append(permutation)

        # list of valid candidates generated
        return self.valid_candidates

    def count_valid_permutations(self):
        """Simple utility method to return the number of valid possibilities"""
        return len(self.get_valid_permutations())

    def get_valid_permutations_refined(self):
        """Utility method to generate a sub list of refined valid password candidates"""
        for permutation in self.valid_candidates:
            if valid_refined(permutation):
                self.valid_candidates_refined.append(permutation)

        # refined list of valid password candidates generated
        return self.valid_candidates_refined

    def count_valid_permutations_refined(self):
        """Utility method to count the number of refined valid password candidates"""
        return len(self.get_valid_permutations_refined())

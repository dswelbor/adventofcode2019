def init_grid(size):
    """
    Simple utility function that initializes a size x size grid using lists
    of lists. Always makes a square grid with odd dimensions
    """
    # creates a list of lists with unique elements valued at 0
    return [[Empty() for j in range(size)] for i in range(size + (size + 1) % 2)]


def resize_grid(grid):
    """
    Utility function to make a new grid double in size and transfer existing entities
    """
    # Initialize a grid roughly
    new_size = 2 * len(grid) + 1
    new_grid = init_grid(new_size)

    # iteratively copy grid into new larger grid
    offset = int((new_size - len(grid)) / 2)
    for i in range (len(grid)):
        for j in range(len(grid)):
            new_grid[i + offset][j + offset] = grid[i][j]

    return new_grid


class WireGrid:
    """
    Class to represent a grid with Wires mapped on it. Provides attributes and behaviors
    to map "wires" onto the grid based a list of "tracing" instructions.
    """
    INITIAL_SIZE = 1021  # Constant defining initial grid size

    def __init__(self):
        """Constructor initializes a wire grid entity"""
        self.grid = init_grid(self.INITIAL_SIZE)
        self.size = self.INITIAL_SIZE
        self.center = (self.size / 2, self.size / 2)
        self.current_pos = {'x': self.center[0], 'y': self.center[1]}

    def trace_wires(self, trace):
        """
        Method maps a series of passed "trace" instructions to the grid. Expected
        instructions are in the form of D123 to go down 123 cells or R03 to go right
        3 cells.
        """
        pass

    def up(self, dist):
        pass

    def down(self, dist):
        pass

    def right(self, dist):
        pass

    def left(self, dist):
        pass


class Empty:
    """Empty Cell entity"""
    def __init__(self):
        """Basic ctor for Empty cell entity"""
        self.taken = False

    """Simple concretion of empty cells"""
    def is_taken(self):
        """Simple utility method that returns false - Cell is not taken"""
        return self.taken

    def __str__(self):
        """Basic __str__ implementation"""
        return ' '


class End:
    """Wire End entity"""
    def __init__(self):
        self.taken = True

    """Simple concretion of a wire endpoint"""
    def is_taken(self):
        """Simple utility method that returns true - cell is taken"""
        return self.taken

    def __str__(self):
        return 'o'


class Wire:
    """Wire connection entity"""
    def __init__(self):
        """Simple ctor for Wire cell entities"""
        self.taken = True

    def is_taken(self):
        """Simple utility method that returns true - cell is taken"""
        return self.taken

    def __str__(self):
        return '.'

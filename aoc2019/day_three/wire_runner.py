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

    def __init__(self, size=INITIAL_SIZE):
        """Initializes a wire grid entity"""
        # 2D list grid - outer list is rows (y), inner list is cols (x)
        # positive is up, east - negative is down, west
        self.grid = init_grid(size)
        self.size = size
        self.center = (int(self.size / 2), int(self.size / 2))
        # Dictionary storing current "position"
        self.current_pos = {'x': self.center[0], 'y': self.center[1]}
        # Map instruction codes to helper methods
        self.instructions = {'U': self.up, 'D': self.down, 'R': self.right, 'L': self.left}
        # Map actions based on cell content
        self.actions = {' ': Wire, '.': Cross}

    def trace_wires(self, trace):
        """
        Method maps a series of passed "trace" instructions to the grid. Expected
        instructions are in the form of D123 to go down 123 cells or R03 to go right
        3 cells.
        """
        # reset "current" position at center
        self.current_pos = {'x': self.center[0], 'y': self.center[1]}
        # iterate through "trace" list
        for opp in trace:
            self.instructions[opp[0]](opp[1:])

    def up(self, dist):
        """Helper method to trace "up" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            current = self.grid[self.current_pos['y'] + offset][self.current_pos['x']]
            # dynamically dispatch action
            self.grid[self.current_pos['y'] + offset][self.current_pos['x']] = \
                self.actions[current.__str__()]()
        # Update "current" coords
        self.current_pos['y'] += dist

    def down(self, dist):
        """Helper method to trace "down" a passed number of cells from current position"""
        # iterate down
        for offset in range(1, dist + 1):
            current = self.grid[self.current_pos['y'] - offset][self.current_pos['x']]
            # dynamically dispatch action
            self.grid[self.current_pos['y'] - offset][self.current_pos['x']] = \
                self.actions[current.__str__()]()
        # Update "current" coords
        self.current_pos['y'] -= dist

    def right(self, dist):
        """Helper method to trace "right" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            current = self.grid[self.current_pos['y']][self.current_pos['x'] + offset]
            # dynamically dispatch action
            self.grid[self.current_pos['y']][self.current_pos['x'] + offset] = \
                self.actions[current.__str__()]()
        # Update "current" coords
        self.current_pos['x'] += dist

    def left(self, dist):
        """Helper method to trace "left" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            current = self.grid[self.current_pos['y']][self.current_pos['x'] - offset]
            # dynamically dispatch action
            self.grid[self.current_pos['y']][self.current_pos['x'] - offset] = \
                self.actions[current.__str__()]()
        # Update "current" coords
        self.current_pos['x'] -= dist


class Empty:
    """Empty Cell entity"""
    def __init__(self):
        """Basic initializer for Empty cell entity"""
        self.taken = False

    def __str__(self):
        """Basic __str__ implementation"""
        return ' '


class End:
    """Wire End entity"""
    def __init__(self):
        self.taken = True

    def __str__(self):
        return 'o'


class Wire:
    """Wire connection entity"""
    def __init__(self):
        """Simple initializer for Wire cell entities"""
        self.taken = True

    def __str__(self):
       return '.'


class Cross:
    """Wire intersection entity"""

    def __init__(self):
        """Simple initializer for "wires crossed" intersection entities"""
        self.taken = True

    def __str__(self):
        return 'x'



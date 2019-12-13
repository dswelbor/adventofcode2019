import sys
from _collections import defaultdict

"""This module provides the logic for day 3 aoc2019 solution with utility functions and classes"""


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


def get_intersections(grid):
    """
    This utility function finds all the intersections in a grid. It returns a list
    of (x, y) tuples
    """
    cross_list = []  # initialize empty list
    # Iterate through all cells in the grid - find intersections
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            # intersection found
            if isinstance(grid[y][x], Cross):
                cross_list.append((x, y))
    return cross_list


def get_min_dist_origin(origin, intersections):
    """
    Utility function that calculates the manhattan distance from origin to
    closest intersection
    """
    # initialize minimum to manhattan dist from origin to far corner
    min_dist = sys.maxsize
    for cross in intersections:
        # calculate manhattan distance from origin to intersection
        x_dist = abs(cross[0] - origin[0])
        y_dist = abs(cross[1] - origin[1])
        dist = x_dist + y_dist
        # assign existing or closer minimum
        min_dist = min(dist, min_dist)

    # return calculated minimum manhattan distance
    return min_dist


class WireGrid:
    """
    Class to represent a grid with Wires mapped on it. Provides attributes and behaviors
    to map "wires" onto the grid based a list of "tracing" instructions. Works when grid is small. Becomes
    unmanageable with large grid sizes.
    """
    INITIAL_SIZE = 1021  # Constant defining initial grid size

    def __init__(self, size=INITIAL_SIZE):
        """Initializes a wire grid entity"""
        # 2D list grid - outer list is rows (y), inner list is cols (x)
        # positive is down, east - negative is up, west
        self.grid = init_grid(size)
        self.size = size
        self.center = (int(self.size / 2), int(self.size / 2))
        # Dictionary storing current "position"
        self.current_pos = {'x': self.center[0], 'y': self.center[1]}
        # Map instruction codes to helper methods
        self.instructions = {'U': self.up, 'D': self.down, 'R': self.right, 'L': self.left}
        # Map actions based on cell content
        self.actions = {' ': Wire, '.': Cross}

    def get_min_manhattan_dist(self):
        """This method returns the manhattan distance from closest intersection from origin"""
        intersections = get_intersections(self.grid)
        dist = get_min_dist_origin(self.center, intersections)
        return dist

    def trace_wires(self, trace):
        """
        Method maps a series of passed "trace" instructions to the grid. Expected
        instructions are in the form of D123 to go down 123 cells or R03 to go right
        3 cells.
        """
        # reset "current" position at center
        self.current_pos = {'x': self.center[0], 'y': self.center[1]}
        # initialize trace point
        self.grid[self.center[1]][self.center[0]] = End()
        # iterate through "trace" list
        for opp in trace:
            #try:
            self.instructions[opp[0]](int(opp[1:]))
            # grid not large enough
            #except IndexError:
            #    self.grid = resize_grid(self.grid)  # enlarge grid
            #    self.size = len(self.grid)  # memoization - store size
            #    self.center = (int(self.size / 2), int(self.size / 2)) # recenter grid
            #    self.instructions[opp[0]](int(opp[1:]))  # try again with "trace" step

    def up(self, dist):
        """Helper method to trace "up" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            try:
                current = self.grid[self.current_pos['y'] - offset][self.current_pos['x']]
                # dynamically dispatch action
                self.grid[self.current_pos['y'] - offset][self.current_pos['x']] = \
                    self.actions[current.__str__()]()
            except IndexError:
                pass  # do nothing
        # Update "current" coords
        self.current_pos['y'] -= dist

    def down(self, dist):
        """Helper method to trace "down" a passed number of cells from current position"""
        # iterate down
        for offset in range(1, dist + 1):
            try:
                current = self.grid[self.current_pos['y'] + offset][self.current_pos['x']]
                # dynamically dispatch action
                self.grid[self.current_pos['y'] + offset][self.current_pos['x']] = \
                    self.actions[current.__str__()]()
            except IndexError:
                pass  # do nothing
        # Update "current" coords
        self.current_pos['y'] += dist

    def right(self, dist):
        """Helper method to trace "right" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            try:
                current = self.grid[self.current_pos['y']][self.current_pos['x'] + offset]
                # dynamically dispatch action
                self.grid[self.current_pos['y']][self.current_pos['x'] + offset] = \
                    self.actions[current.__str__()]()
            except IndexError:
                pass  # do nothing
        # Update "current" coords
        self.current_pos['x'] += dist

    def left(self, dist):
        """Helper method to trace "left" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            try:
                current = self.grid[self.current_pos['y']][self.current_pos['x'] - offset]
                # dynamically dispatch action
                self.grid[self.current_pos['y']][self.current_pos['x'] - offset] = \
                    self.actions[current.__str__()]()
            except IndexError:
                pass  # do nothing
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


class WireTable:
    """
    Class represents wire "traces" as dictionaries with x coordinate keys and y
     coordinates appended to keyed lists
    """
    def __init__(self):
        self.traces = []  # list of dictionaries with wire "traces"
        self.trace_list = []  # list of trace instructions
        # initialize grid cursor position at origin
        self.current_x = 0
        self.current_y = 0
        self.current_steps = 0  # counter for steps
        self.current_trace = None  # dictionary of current trace
        self.intersections = None  # list of intersection tuples
        self.list_keyed_intersect_steps = None  # list of dictionaries of steps per intersection
        self.current_intersect_steps = None  # dictionary of current steps
        # Map instruction codes to helper methods
        self.instructions = {'U': self.up, 'D': self.down, 'R': self.right, 'L': self.left}
        # Map instruction codes to helper methods
        self.count_steps_instr = {'U': self.up_count, 'D': self.down_count, 'R': self.right_count, 'L': self.left_count}

    def trace_wires(self, trace):
        """
        Method maps a series of passed "trace" instructions to the trace dictionaries. Expected
        instructions are in the form of D123 to go down 123 cells or R03 to go right
        3 cells.
        """
        # save a reference to the list
        self.trace_list.append(trace)
        # reset "current" position at center
        self.current_x = 0
        self.current_y = 0
        # initialize trace dictionary
        self.current_trace = defaultdict(list)
        # iterate through "trace" list
        for opp in trace:
            self.instructions[opp[0]](int(opp[1:]))

        # add current_trace to list of traces
        self.traces.append(self.current_trace)
        self.current_trace = None

    def get_min_manhattan_dist(self):
        """This method returns the manhattan distance from closest intersection from origin"""
        # generate intersections
        self.find_intersections()
        # get manhattan distance to closest
        dist = get_min_dist_origin((0, 0), self.intersections)
        return dist

    def find_intersections(self):
        """Helper method that iteratively saves list of intersections for both traces"""
        self.intersections = []
        # iterate through
        for x_trace1 in self.traces[0]:
            try:
                # iterate through y values
                for y_trace1 in self.traces[0][x_trace1]:
                    # see if coord x, y pair is present in both traces
                    if x_trace1 != 0 and y_trace1 in self.traces[1][x_trace1]:
                        self.intersections.append((x_trace1, y_trace1))
                pass
            except KeyError:
                pass  # do nothing - no matching pairs at this x value

    def find_min_steps(self):
        self.list_keyed_intersect_steps = []
        for trace in self.trace_list:
            self.current_intersect_steps = {}
            # reset "current" position at center
            self.current_x = 0
            self.current_y = 0
            # reset step counter
            self.current_steps = 0
            # iterate through "trace" list
            for opp in trace:
                self.count_steps_instr[opp[0]](int(opp[1:]))
            # Append
            self.list_keyed_intersect_steps.append(self.current_intersect_steps)

        # calculate sum of steps to a given intersection
        min_steps = sys.maxsize
        for cross in self.intersections:
            steps = self.list_keyed_intersect_steps[0][cross] + self.list_keyed_intersect_steps[1][cross]
            min_steps = min(steps, min_steps)
        # minimum number of steps to intersection calculated
        return min_steps

    def up(self, dist):
        """Helper method to trace "up" a passed number of cells from current position"""
        # iterate up
        for offset in range(1, dist + 1):
            self.current_trace[self.current_x].append(self.current_y + offset)
        # Update "current" coords
        self.current_y += dist

    def down(self, dist):
        """Helper method to trace "down" a passed number of cells from current position"""
        # iterate down
        for offset in range(1, dist + 1):
            self.current_trace[self.current_x].append(self.current_y - offset)
        # Update "current" coords
        self.current_y -= dist

    def right(self, dist):
        """Helper method to trace "right" a passed number of cells from current position"""
        # iterate right
        for offset in range(1, dist + 1):
            self.current_trace[self.current_x + offset].append(self.current_y)
        # Update "current" coords
        self.current_x += dist

    def left(self, dist):
        """Helper method to trace "left" a passed number of cells from current position"""
        # iterate left
        for offset in range(1, dist + 1):
            self.current_trace[self.current_x - offset].append(self.current_y)
        # Update "current" coords
        self.current_x -= dist

    def up_count(self, dist):
        """
        Helper method to trace "up" a passed number of cells from current position
        and count steps to and intersection.
        """
        # iterate up
        for offset in range(1, dist + 1):
            self.current_steps += 1  # increment step counter
            # currently at
            if (self.current_x, self.current_y + offset) in self.intersections:
                self.current_intersect_steps[(self.current_x, self.current_y + offset)] = self.current_steps

        # Update "current" coords
        self.current_y += dist

    def down_count(self, dist):
        """
        Helper method to trace "down" a passed number of cells from current position
        and count steps to and intersection.
        """
        # iterate down
        for offset in range(1, dist + 1):
            self.current_steps += 1  # increment step counter
            # currently at
            if (self.current_x, self.current_y - offset) in self.intersections:
                self.current_intersect_steps[(self.current_x, self.current_y - offset)] = self.current_steps
        # Update "current" coords
        self.current_y -= dist

    def right_count(self, dist):
        """
        Helper method to trace "right" a passed number of cells from current position
        and count steps to and intersection.
        """
        # iterate right
        for offset in range(1, dist + 1):
            self.current_steps += 1  # increment step counter
            # currently at
            if (self.current_x + offset, self.current_y) in self.intersections:
                self.current_intersect_steps[(self.current_x + offset, self.current_y)] = self.current_steps
        # Update "current" coords
        self.current_x += dist

    def left_count(self, dist):
        """
        Helper method to trace "left" a passed number of cells from current position
        and count steps to and intersection.
        """
        # iterate left
        for offset in range(1, dist + 1):
            self.current_steps += 1  # increment step counter
            # currently at
            if (self.current_x - offset, self.current_y) in self.intersections:
                self.current_intersect_steps[(self.current_x - offset, self.current_y)] = self.current_steps
        # Update "current" coords
        self.current_x -= dist

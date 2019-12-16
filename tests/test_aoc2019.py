#!/usr/bin/env python
import pytest
from aoc2019.day_one import day_one_util
from aoc2019.shared import int_code
from aoc2019.day_three import wire_runner
from aoc2019.day_three.wire_runner import Empty, End, Wire, WireGrid, WireTable
from aoc2019.day_four.container_cracker import valid, valid_refined

"""Tests for `aoc2019` package."""

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_day_one_part_one():
    """Test case: compare the algorithm with sample data provided for day 1 part 1"""
    assert 34241 == day_one_util.calc_fuel_reqs('tests/test_day1.txt'), 'Day one part one failed'


def test_day_one_part_two():
    """Test caseL compare the algorithm with sample day for day 1 part 2"""
    assert 2 == day_one_util.calc_module_fuel(14)
    assert 50346 == day_one_util.calc_module_fuel(100756)


def test_day_two_int_code_init():
    """Test case: Assert IntCode object instantiates correctly"""
    test_list = [1, 0, 0, 99]
    test_obj = int_code.IntCode(test_list)
    assert 4 == len(test_obj.list)


def test_day_two_int_code_visit():
    """Test case: Assert IntCode object appropriately visits an object"""
    test_list = [1, 0, 0, 0, 99]
    test_obj = int_code.IntCode(test_list)
    test_obj.visit()  # Expect [2, 0, 0, 0, 99]
    print(test_obj.list)
    assert 2 == test_obj.list[0]


def test_day_two_int_code_visit_all():
    """Test case: Assert IntCode object appropriately visits all objects"""
    # test list 1
    test_list = [2, 4, 4, 5, 99, 0]
    test_obj = int_code.IntCode(test_list)
    test_obj.visit_all()  # Expect [2, 4, 4, 5, 99, 9801]
    print(test_obj.list)
    assert 9801 == test_obj.list[5]

    # test list 2
    test_list2 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    test_obj2 = int_code.IntCode(test_list2)
    test_obj2.visit_all()  # Expect [30, 1, 1, 4, 2, 5, 6, 0, 99]
    print(test_obj2.list)
    assert 30 == test_obj2.list[0]
    assert 2 == test_obj2.list[4]

    # test list 3
    test_list3 = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19,
                  1, 19, 6, 23, 2, 23, 13, 27, 1, 27, 5, 31, 2, 31, 10, 35, 1, 9,
                  35, 39, 1, 39, 9, 43, 2, 9, 43, 47, 1, 5, 47, 51, 2, 13, 51, 55,
                  1, 55, 9, 59, 2, 6, 59, 63, 1, 63, 5, 67, 1, 10, 67, 71, 1, 71,
                  10, 75, 2, 75, 13, 79, 2, 79, 13, 83, 1, 5, 83, 87, 1, 87, 6, 91,
                  2, 91, 13, 95, 1, 5, 95, 99, 1, 99, 2, 103, 1, 103, 6, 0, 99, 2, 14, 0, 0]
    test_obj3 = int_code.IntCode(test_list3)
    test_obj3.visit_all()
    print(test_obj3.list)
    assert 3790645 == test_obj3.list[0]


def test_day_three_grid_resize():
    """Test case: initialize a new grid and test the grid for accuracy after resize"""
    initial_grid = wire_runner.init_grid(3)
    expected_grid = [[Empty(), Empty(), Empty()],
                     [Empty(), Empty(), Empty()],
                     [Empty(), Empty(), Empty()]]
    # Test initial default empty values
    for i in range(len(initial_grid)):
        for j in range(len(initial_grid)):
            assert expected_grid[i][j].__str__() == initial_grid[i][j].__str__()

    # Test resized grid
    initial_grid[1][0] = End()
    initial_grid[1][1] = Wire()
    initial_grid[1][2] = End()
    initial_grid[0][2] = End()
    resized_grid = wire_runner.resize_grid(initial_grid)
    expected_resized = [[Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                        [Empty(), Empty(), Empty(), Empty(), End(), Empty(), Empty()],
                        [Empty(), Empty(), End(), Wire(), End(), Empty(), Empty()],
                        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()]]
    for i in range(len(resized_grid)):
        for j in range(len(resized_grid)):
            assert expected_resized[i][j].__str__() == resized_grid[i][j].__str__()


def test_day_three_trace_wires():
    """Test case: "trace" a series of instructions and assert grid matches expected output"""
    test_list = ['R8', 'U5', 'L5', 'D3']
    test_wire_grid = WireGrid(size=17)
    test_wire_grid.trace_wires(test_list)
    expected_test_grid = [[Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],

                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Wire(), Wire(), Wire(), Wire(), Wire(), Wire()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Wire(), Empty(), Empty(), Empty(), Empty(), Wire()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Wire(), Empty(), Empty(), Empty(), Empty(), Wire()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Wire(), Empty(), Empty(), Empty(), Empty(), Wire()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Wire()],

                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), End(), Wire(), Wire(), Wire(), Wire(), Wire(), Wire(), Wire(), Wire()],

                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],

                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
                          [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],]

    for i in range(17):
        for j in range(17):
            assert expected_test_grid[i][j].__str__() == test_wire_grid.grid[i][j].__str__()


def test_day_three_get_intersections():
    """
    Test case: This test "traces" a list of 2 sets of instructions, then uses
    get_intersections method to return a list of intersection tuples. Asserts list
    of tuples matches expected output.
    """
    test_list1 = ['R8', 'U5', 'L5', 'D3']
    test_list2 = ['U7', 'R6', 'D4', 'L4']
    # instantiate Wire grade and trace instructions
    test_wire_grid = WireGrid(size=17)
    test_wire_grid.trace_wires(test_list1)  # trace first input list
    test_wire_grid.trace_wires(test_list2)  # trace second input list

    # get intersection list
    tuples = wire_runner.get_intersections(test_wire_grid.grid)
    # (12, 6), (15, 4)
    assert tuples == [(14, 3), (11, 5)]


def test_day_three_get_min():
    """
    Test case: Pass 2 sets of "trace" instructions to WireGrid and verify
    manhattan distance to intersection closest to origin.
    """
    # R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    # U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
    test_list1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    test_list2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    test_wire_grid = WireGrid()
    test_wire_grid.trace_wires(test_list1)  # trace first input list
    test_wire_grid.trace_wires(test_list2)  # trace second input list

    # get manhattan dist
    dist = test_wire_grid.get_min_manhattan_dist()
    assert 135 == dist


def test_day_three_get_min_wire_table():
    """
    Test case: Pass 2 sets of "trace" instructions to WireTable and verify manhattan
    distance to intersection closest to origin.
    """
    test_list1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    test_list2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    test_wire_table = WireTable()
    test_wire_table.trace_wires(test_list1)  # trace first input list
    test_wire_table.trace_wires(test_list2)  # trace second input list
    # get manhattan dist
    dist = test_wire_table.get_min_manhattan_dist()
    assert 135 == dist

    # R75,D30,R83,U83,L12,D49,R71,U7,L72
    # U62,R66,U55,R34,D71,R55,D58,R83
    test_list3 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    test_list4 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    test_wire_table2 = WireTable()
    test_wire_table2.trace_wires(test_list3)  # trace third input list
    test_wire_table2.trace_wires(test_list4)  # trace fourth input list
    # get manhattan dist
    dist = test_wire_table2.get_min_manhattan_dist()
    assert 159 == dist


def test_day_three_find_min_steps():
    """
    Test case: Pass 2 sets of "trace" instructions to WireTable and verify manhattan
    distance to intersection closest to origin.
    """
    test_list1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    test_list2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    # test_list1 = ['R8', 'U5', 'L5', 'D3']
    # test_list2 = ['U7', 'R6', 'D4', 'L4']
    test_wire_table = WireTable()
    test_wire_table.trace_wires(test_list1)  # trace first input list
    test_wire_table.trace_wires(test_list2)  # trace second input list
    # get manhattan dist
    dist = test_wire_table.get_min_manhattan_dist()
    steps = test_wire_table.find_min_steps()
    assert 410 == steps

    # R75,D30,R83,U83,L12,D49,R71,U7,L72
    # U62,R66,U55,R34,D71,R55,D58,R83
    test_list3 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    test_list4 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    test_wire_table2 = WireTable()
    test_wire_table2.trace_wires(test_list3)  # trace third input list
    test_wire_table2.trace_wires(test_list4)  # trace fourth input list
    # get manhattan dist
    dist = test_wire_table2.get_min_manhattan_dist()
    steps = test_wire_table2.find_min_steps()
    assert 610 == steps


def test_day_four_is_valid():
    """
    Test case: Assert that the valid function appropriately returns true for
    valid input.
    """
    test_one = 111111
    test_two = 223450
    test_three = 123789
    test_four = 128888
    assert valid(test_one)
    assert not valid(test_two)
    assert not valid(test_three)
    assert valid(test_four)


def test_day_four_is_valid_refined():
    """
    Test case: Assert that the valid_refined function appropriately returns
    true for valid input.
    """
    test_one = 112233
    test_two = 123444
    test_three = 111122
    test_four = 127889
    assert valid_refined(test_one)
    assert not valid_refined(test_two)
    assert valid_refined(test_three)
    assert valid_refined(test_four)


def test_day_five_add_opp():
    """
    Test case: Assert that add_opp with immediate mode enabled works as intended.
    """
    # [1101,100,-1,4,0]
    test_list = [1101, 100, -1, 4, 0]
    test_obj = int_code.IntCode(test_list)
    test_obj.visit_all()  # Expect ---
    print(test_obj.list)
    assert 99 == test_obj.list[4]


def test_day_five_jump_position():
    """Test case: Assert that jump functions work with position mode."""
    test_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    test_obj = int_code.IntCode(test_list[:])
    test_obj.run(0)
    assert 0 == test_obj.output_codes[-1]

    # try with input 1
    test_obj2 = int_code.IntCode(test_list[:])
    test_obj2.run(1)
    assert 1 == test_obj2.output_codes[-1]


def test_day_five_jump_immediate():
    """Test case: Assert that jump functions work with immediate mode"""
    test_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    test_obj = int_code.IntCode(test_list[:])
    test_obj.run(0)
    assert 0 == test_obj.output_codes[-1]

    # try with input 1
    test_obj2 = int_code.IntCode(test_list[:])
    test_obj2.run(4)
    assert 1 == test_obj2.output_codes[-1]


def test_day_five_equals_position():
    """Test case: Assert that equals method works with position mode."""
    # [3,9,8,9,10,9,4,9,99,-1,8]
    test_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    test_obj = int_code.IntCode(test_list.copy())
    test_obj.run(8)
    assert 1 == test_obj.output_codes[-1]


def test_day_five_equals_immediate():
    """Test case: Assert that equals method works with position mode."""
    # [3,3,1108,-1,8,3,4,3,99]
    test_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    test_obj = int_code.IntCode(test_list.copy())
    test_obj.run(8)
    assert 1 == test_obj.output_codes[-1]

    # test input not == 8
    test_obj = int_code.IntCode(test_list.copy())
    test_obj.run(9)
    assert 0 == test_obj.output_codes[-1]


def test_day_five_less_position():
    """Test case: Assert that equals method works with position mode. Expect output 0 - not less than 8"""
    # 3,9,7,9,10,9,4,9,99,-1,8
    # input not < 8
    test_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    test_obj = int_code.IntCode(test_list.copy())
    test_obj.run(8)
    assert 0 == test_obj.output_codes[-1]

    # try with input < 8
    test_obj2 = int_code.IntCode(test_list.copy())
    test_obj2.run(7)
    assert 1 == test_obj2.output_codes[-1]


def test_day_five_less_immediate():
    """Test case: Assert that equals method works with position mode. Expect output 0 - not less than 8"""
    # 3,3,1107,-1,8,3,4,3,99
    # input not < 8
    test_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    test_obj = int_code.IntCode(test_list.copy())
    test_obj.run(8)
    assert 0 == test_obj.output_codes[-1]

    # try with input < 8
    test_obj2 = int_code.IntCode(test_list.copy())
    test_obj2.run(7)
    assert 1 == test_obj2.output_codes[-1]



def test_day_five_run_input():
    """
    Test case: Assert that new methods produce expected output diagnostic code
    for provided input.
    """
    test_list = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006,
                 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20,
                 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4,
                 20, 1105, 1, 46, 98, 99]
    test_obj = int_code.IntCode(test_list.copy())
    test_obj.run(7)
    assert 999 == test_obj.output_codes[-1]

    # test with input = 8
    test_obj2 = int_code.IntCode(test_list.copy())
    test_obj2.run(8)
    assert 1000 == test_obj2.output_codes[-1]

    # test with input > 8
    test_obj3 = int_code.IntCode(test_list.copy())
    test_obj3.run(9)
    assert 1001 == test_obj3.output_codes[-1]

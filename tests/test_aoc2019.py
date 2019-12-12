#!/usr/bin/env python

"""Tests for `aoc2019` package."""

import pytest
from aoc2019.day_one import day_one_util
from aoc2019.day_two import int_code
from aoc2019.day_three import wire_runner
from aoc2019.day_three.wire_runner import Empty, End, Wire, WireGrid

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

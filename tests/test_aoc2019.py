#!/usr/bin/env python

"""Tests for `aoc2019` package."""

import pytest
from aoc2019.day_one import day_one_util
from aoc2019.day_two import int_code


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
    test_list = [2, 4, 4, 5, 99, 0]
    test_obj = int_code.IntCode(test_list)
    test_obj.visit_all()  # Expect [2, 4, 4, 5, 99, 9801]
    print(test_obj.list)
    assert 9801 == test_obj.list[5]




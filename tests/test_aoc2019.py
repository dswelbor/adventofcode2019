#!/usr/bin/env python

"""Tests for `aoc2019` package."""

import pytest


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


@pytest.fixture
def day_one_part_one():
    from day_one import day_one
    assert 34241 == day_one.calc_fuel_reqs('test.txt'), 'Day one part one failed'



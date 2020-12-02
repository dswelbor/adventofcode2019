===================
Advent of Code 2020
===================


.. image:: https://travis-ci.com/dswelbor/advent2019.svg?branch=master
        :target: https://travis-ci.com/dswelbor/advent2019

Solutions to AdventofCode2020 challenges implemented in python.
Advent of Code: http://adventofcode.com/

* Free software: MIT license

Poetry
------
This project utilizes poetry for managing python dependencies and freezing
versions as necessary. Multiple methods of installation are available - including
using pip (not preferred). More information can be found at:
https://python-poetry.org/docs/

Instructions
------------
TODO : Update to reflect new solutions
To run each day solution, from the ``aoc2020`` module, run the
command:
``python3 run_day_<DAY_NUMBER>.py``

For example, to run the day one challenge solution, from ``aoc2019``, run:

``python3 run_day_one.py``

Unit Testing
------------
Unit tests for each solution are available in ``tests/``. To run the full
complement of unit test, use the following command: ``poetry run pytest``

Alternatively, to run tests from a particular testing file, use the filename
as an argument. For example, to run the test for aoc2020, execute the
following command: ``poetry run pytest tests/test_aoc2019.py``

Features
--------

* Day One solution
    using iterative sums

* Day Two solution
    using dynamic dispatch to replace conditionals with polymorphism and apply short-circuited brute force logic

* Day Three solution
    using dynamic dispatch to increment a "current position" and generate a collection of "traced" (x, y) tuples.
    It generates a collection of intersection coordinate tuples and returns about the distance from origin to
    "closest" intersection.

* Day Four solution
    using validation to iteratively generate a list of "valid" permutations, refine this
    list of permutations based on additional criteria, and return a count of valid permutation
    candidates for both sets of requirements.

* Day Five solution
    re-using the IntCode class from Day Two. IntCode was refactored to use more dynamic dispatch for handling
    int codes and opp code parameters, adding new functionality while supporting prior prior requirements.

* Day Six solution
    using Composite and Builder design patterns to construct a tree. Recursively caounts all direct and
    indirect edge relations.  Additionally implements an Iterator using level order traversal to handle edge
    distance calculations.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Included input text data was provided as a part of the Advent of Code 2019 challenge. http://adventofcode.com/

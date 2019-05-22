#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the Project1 module.
"""
import pytest
import requests
from unittest.mock import patch
from Project1 import project1


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise (ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_Project1(an_object):
    assert an_object == {}


def test_addNumbers():
    assert project1.addNumbers(1, 1) == 2


def test_wordCount():
    book = 'https://www.gutenberg.org/files/59551/59551-0.txt'
    wc = project1.wordCount(book)
    assert wc == 82738

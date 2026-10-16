import pytest
from tools.collatz_sequence import run


def test_collatz_sequence_basic():
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert run("6") == "6,3,10,5,16,8,4,2,1"
    assert run("1") == "1"
    assert run("2") == "2,1"
    assert run("3") == "3,10,5,16,8,4,2,1"
    assert run("4") == "4,2,1"
    assert run("5") == "5,16,8,4,2,1"
    assert run(" 6 ") == "6,3,10,5,16,8,4,2,1"


def test_collatz_sequence_errors():
    assert run() == "Error: expected an integer"
    assert run("") == "Error: expected an integer"
    assert run("   ") == "Error: expected an integer"
    assert run("abc") == "Error: argument must be an integer"
    assert run("1.5") == "Error: argument must be an integer"
    assert run("0") == "Error: argument must be a positive integer"
    assert run("-6") == "Error: argument must be a positive integer"

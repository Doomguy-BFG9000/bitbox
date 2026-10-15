from tools.word_lengths import run


def test_word_lengths_example():
    assert run("hi there") == "2,5"


def test_single_word():
    assert run("hello") == "5"


def test_multiple_words():
    assert run("hello world python") == "5,5,6"


def test_multiple_spaces_between_words():
    assert run("hi   there") == "2,5"


def test_empty_string():
    assert run("") == "0"


def test_whitespace_only_string():
    assert run("   ") == "0"


def test_missing_argument():
    assert run() == "Error: requires a string argument"


def test_none_argument():
    assert run(None) == "Error: requires a string argument"

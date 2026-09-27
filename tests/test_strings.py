"""Tiny deterministic string suite (matrix leg: suite=strings)."""


def shout(s: str) -> str:
    return s.upper() + "!"


def test_shout():
    assert shout("hello") == "HELLO!"


def test_shout_empty():
    assert shout("") == "!"


def test_shout_already_upper():
    assert shout("OK") == "OK!"

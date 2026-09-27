"""Tiny deterministic arithmetic suite (matrix leg: suite=calc)."""


def add(a: int, b: int) -> int:
    return a + b


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-4, 4) == 0


def test_add_zero():
    assert add(0, 0) == 0

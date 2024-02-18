from src import code


def test_sum_numbers():
    assert code.sum_numbers(1, 2) == 3


def test_sum_numbers_fail():
    assert code.sum_numbers(1, 2) != 2

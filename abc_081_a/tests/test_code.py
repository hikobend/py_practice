from src import code


def test_correct_count_number():
    assert code.count_number("10011001111") == 7
    assert code.count_number("00000000000") == 0
    assert code.count_number("11111111111") == 11
    assert code.count_number("10101010101") == 6


def test_incorrect_count_number():
    assert code.count_number("10011001111") != 6
    assert code.count_number("00000000000") != 1
    assert code.count_number("11111111111") != 10
    assert code.count_number("10101010101") != 5

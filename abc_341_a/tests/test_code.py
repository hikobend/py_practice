from src import code


def test_correct_show_number():
    assert code.show_number(3) == "0101011"
    assert code.show_number(5) == "01010101011"


def test_incorrect_show_number():
    assert code.show_number(3) != "010101"
    assert code.show_number(5) != "10101010101"

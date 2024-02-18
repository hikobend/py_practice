from src import code


def test_culc_odd():
    assert code.culc(3, 3) == "奇数"
    assert code.culc(2, 3) != "奇数"


def test_culc_even():
    assert code.culc(2, 2) == "偶数"
    assert code.culc(3, 2) == "偶数"
    assert code.culc(3, 3) != "偶数"


def test_culc_error():
    assert code.culc(1.1, 2) == "error"

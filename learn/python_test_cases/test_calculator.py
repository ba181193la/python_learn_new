from calculator import add, subtract


def test_add():
    result = add(10, 20)

    assert result == 30


def test_subtract():
    result = subtract(20, 10)

    assert result == 10
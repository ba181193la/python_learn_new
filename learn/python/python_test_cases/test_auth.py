from auth import login


def test_valid_login():
    result = login("bala", "1234")

    assert result == True


def test_wrong_password():
    result = login("bala", "wrong")

    assert result == False


def test_wrong_username():
    result = login("wrong", "12345")

    assert result == False
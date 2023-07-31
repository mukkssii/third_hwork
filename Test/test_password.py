import password


def test_valid_pass():
    assert password.valid_pass(password='Password@=1234') is True
    assert password.valid_pass(password='assword@=1234') is False
    assert password.valid_pass(password='PASSWORD@=1234') is False
    assert password.valid_pass(password='Password1234') is False
    assert password.valid_pass(password='Password@ 1234') is False
    assert password.valid_pass(password='Password@=') is False
    assert password.valid_pass(password='Pa!123') is False
    assert password.valid_pass(password='пароль@=1234') is False

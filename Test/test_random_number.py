import random
import random_number


def test_random_number():
    assert 1 <= random_number.random_number(number=random.randint(1, 1001)) <= 1000

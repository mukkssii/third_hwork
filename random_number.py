import random


def random_number(number: int):
    for number in range(1001):
        number = random.randint(1, 1001)
    return number


result = random_number(number=random.randint(1, 1001))
print(result)

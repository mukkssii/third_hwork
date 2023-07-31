def valid_pass(password: str,
               is_valid_length=False,
               is_valid_contains_upper=False,
               is_valid_contains_lower=False,
               contains_special_symbols=False,
               is_valid_contains_digits=False,
               is_valid_spaces=True,
               is_valid_only_latin=False) -> bool:

    if len(password) >= 8:
        is_valid_length = True

    for letter in password:
        if letter.isdigit():
            is_valid_contains_digits = True

        if letter.isupper():
            is_valid_contains_upper = True

        if letter.islower():
            is_valid_contains_lower = True

        if letter in '+-/*!"№;%:?*()=':
            contains_special_symbols = True

        if letter in ' ':
            is_valid_spaces = False

        if letter.isascii():
            is_valid_only_latin = True

    return all([is_valid_length,
                is_valid_contains_upper,
                is_valid_contains_lower,
                contains_special_symbols,
                is_valid_contains_digits,
                is_valid_spaces,
                is_valid_only_latin
                ])


print(valid_pass(password='Password@=1234'))

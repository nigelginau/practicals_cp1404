"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 20
MAX_LENGTH = 26
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_checker = 0
    count_special = 0

    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        count_lower = int(char.islower()) + count_lower
        count_upper = int(char.isupper()) + count_upper
        count_digit = int(char.isdigit()) + count_digit
        count_list = (count_lower, count_upper, count_digit)
        count_checker = sum(count_list)
        normal_count = int(char.islower()) + int(char.isupper()) + int(char.isdigit())
        pass
    # TODO: if length is wrong, return False
    if len(password) > 6 or len(password) < 2:
        return False

    # TODO: if any of the 'normal' counts are zero, return False

    elif count_checker < 5:
        return False
    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    else:
        count_special = 6 - count_checker
        SPECIAL_CHARS_REQUIRED = True

    return True


main()

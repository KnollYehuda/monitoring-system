from random import choice
from string import ascii_lowercase


def string_generator(length: int = 50):
    """Generate a random string of lowercase letters.

    :param length: The length of the generated string. Defaults to 50.
    :return randomly generated string of lowercase letters.
    """

    return "".join(choice(ascii_lowercase) for _ in range(length))

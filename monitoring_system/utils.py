from random import choice
from string import ascii_lowercase


def string_generator(length: int = 50):
    return "".join(choice(ascii_lowercase) for _ in range(length))

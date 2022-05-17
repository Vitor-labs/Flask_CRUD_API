import string
import random


random_generator = random.SystemRandom(random.randint(0, 2**32))


def random_string(length=10):
    return ''.join(random_generator.choice(string.ascii_lowercase) for _ in range(length))


key = random_string(50)

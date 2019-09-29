import string
import random

def random_string_alphanum(length = 10):
        alphabet = string.ascii_letters + string.digits

        return ''.join(random.choice(alphabet) for _ in range(length))

def random_string_ASCII(length = 10):
        alphabet = string.ascii_letters

        return ''.join(random.choice(alphabet) for _ in range(length))

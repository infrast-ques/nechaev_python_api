import random
import string


class Utils:
    @staticmethod
    def get_random_string(length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

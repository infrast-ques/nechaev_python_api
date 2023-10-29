class Culculator:
    random_val = 0

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def diff(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    # Целая часть от деления
    def mod_div(a, b):
        return a // b


result = Culculator.diff(5, 3)
print(result)

print(eval("2**2"))

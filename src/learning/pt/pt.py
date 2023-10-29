from functools import wraps


def my_resolution(obj, indent=0):
    if isinstance(obj, str):
        print('\t' * indent + obj)
        indent = 0
    if isinstance(obj, dict):
        for key, value in obj.items():
            print('\t' * indent, key)
            my_resolution(value, indent + 1)


my_resolution({
    '1': {
        'child': '1/child/value'
    },
    '2': '2/value'
})


def print_dict(value):
    for key, value in value.items():
        print(key)
        print('\t' + value)


print_dict({
    'first': 'first_value',
    'second': 'second_value'
})

#  1 Задание - перевернуть строку
string = "ninja turtles"
# Мое решение
# new_string = ""
# for char in string[::-1]:
#     new_string += char
# string = new_string
# print(string)
# Нормально решение
string = string[::-1]
print(string)

# 2 Задание, нужно посчитать вхождение каждой буквы
string = "asdasdmpmqoiwmrosnfpisdmfksdnmfisdipjfninsddomaofjndsipfhnsd"
result = {}
# for char in string:
#     count = result.get(char)
#     if count is None:
#         result.update({char: 1})
#     else:
#         count += 1
#         result.update({char: count})

for char in string:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
print(result)


def decorator(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return inner


@decorator
def return_int(num):
    return num


func = return_int(5)
print(func)


def decorator2(arg):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * arg

        return inner

    return wrapper


@decorator2(5)
def return_int2(num):
    return num


func = return_int2(5)
print(func)

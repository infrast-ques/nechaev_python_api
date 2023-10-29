import math
import operator
from functools import reduce, wraps
from operator import mul


def f(*args):
    print(type(args))
    if len(args) == 0:
        print(args)
        print(())
    else:
        print(args[0])


f()
# => tuple
# => ()

f(1, 'a', None, False)


# => tuple
# => (1, 'a', None, False)


def f(x, *args):
    print(f'Первый аргумент: {x}')
    for a in args:
        print(f'Другой аргумент из *args {a}!')


f('Programing language', 'Python', 'PHP', 'Java')


def sum1(a, b):
    return a + b


nums = [3, 4]
print(sum1(*nums))


def greet(*names):
    for name in names:
        print(name)


greet('Bob',
      *['Mary', 'Clair'],
      'Sam',
      *('Henry', 'John')
      )


def greet(first_name, *name):
    return f'Hello, {" and ".join((first_name,) + name)}!'


print(greet('Bob', 'Ann'))


def f(*args, **kwargs):
    return (*args, kwargs)


# result = f(1, 2, 3, 4, qw='qw', we='we')


# print(result)


def open_file(name, *, writable=False, binary=False):
    pass


f1 = open_file('foo.txt', writable=True)
f2 = open_file('bar.bin', binary=True)


# f3 = open_file('raw.dat', True, True)

def updated(di: dict, **kwargs):
    new_dict = di.copy()
    new_dict.update(kwargs)
    return new_dict


def updated1(di: dict, **kwargs):
    return {**di, **kwargs}


d = {'a': 1, 'b': False}
print(updated(d, a=2, b=True, c=None))
print(updated(d))


def my_print_name(first_name, last_name):
    print(first_name, last_name)


my_name_dict = (
    {
        "first_name": "roman",
        "last_name": "nechaev"
    },
    {
        "first_name": "yana",
        "last_name": "larina"
    },
    {
        "first_name": "ivan",
        "last_name": "valutin"
    },)

for name in my_name_dict:
    my_print_name(**name)


def get_unique(*args):
    unique_list = []
    for lst in args:
        for item in lst:
            if item not in unique_list:
                unique_list.append(item)
    return unique_list


# print(get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7]))7
data1 = [[1, 2, 3], [3, 2, 4], [4, 1, 5, 6]]
result = get_unique(*data1)
print(result)

my_fun = get_unique
result = my_fun(*data1)
print(result)


def apply_function(numbers, function):
    return [function(number) for number in numbers]


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function(numbers, square)
print(squared_numbers)


# [1, 4, 9, 16, 25]


def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5))  # 10
print(times_3(5))  # 15


def get_first_name(fill_name: str):
    return fill_name.split("_")[0]


def sort_by(func, users):
    return sorted(users, key=lambda user: func(user), reverse=True)


users = ["Obi-Wan_Kenobi", "Jabba_Hutt", "Princess_Leia"]

result = sort_by(get_first_name, users)  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
print(result)  # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

# def reduce(func, values, init_value):
#     result = init_value
#     for value in values:
#         result = func(result, value)
#     return result


print(reduce(lambda r, v: r * v, [1, 2, 3, 4, 5], 1))


def filter_map(func, item_list):
    result = []
    for item in item_list:
        i_filter, i_map = func(item)
        if i_filter:
            result.append(i_map)

    return result


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)


# => *
# => *****
# => **


def say_prime_or_not(number):
    result = "yes"
    if number <= 1:
        result = "no"
    for n in range(2, number - 1):
        if number % n == 0:
            result = "no"
    print(result)


numbers = [9, 10, 11, 12, 13]
result = list(map(say_prime_or_not, numbers))

numbers = [2, 3, 8, 11, 10, 100, 1, 2, 5, 6, 99]


def get_maximum(first_num, second_num):
    return first_num if first_num > second_num else second_num


print(reduce(get_maximum, numbers, 10))  # 10
reduce(get_maximum, numbers)  # 8

map(mul, "abc", [3, 5, 7])  # <map object at ...>
print(list(map(mul, "abc", [3, 5, 7])))  # ['aaa', 'bbbbb', 'ccccccc']

print(list(filter(None, ['', 1, 2, 'foo', None, False])))


def keep_truthful(iterable):
    return filter(operator.truth, iterable)


FALSES = (False, (), None, '', 0)
TRUTHS = (True, (1,), '!', -5)
print(list(keep_truthful(FALSES)))
print(list(keep_truthful(TRUTHS)))
print(list(keep_truthful([0, 1, 0])))


# [True, 'foo']

def abs_sum(nums):
    return list(map(lambda num: abs(num), nums))


print(abs_sum([0]))
# 10
print(abs_sum((-42,)))
# 0
print(abs_sum([-3, -2, -1, 0, 1, 2]) == 12)


# 42


def walk(diсt, path):
    result = diсt
    for item in path:
        result = result.__getitem__(item)
    return result


city = {
    'Pine': {
        '5': 'School #42',
    },
    'Elm': {
        '13': {
            '1': 'Appartments #2, Elm st.13',
        },
    },
}
print(walk(city, ['Pine', '5']) == city['Pine']['5'])
path = ['Elm', '13', '1']
print(walk(city, path) == city['Elm']['13']['1'])


# {'b': 42}


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure = outer_function(10)
print(closure(5))  # => 15
print(closure(10))  # => 15


# def greet(name, surname):
#     return f'Hello, {name} {surname}!'
#
#
# def partial_apply(func, name_user):
#     def inner(surname):
#         return func(name_user, surname)
#
#     return inner
#
#
# f = partial_apply(greet, 'Dorian')
# print(f('Grey'))
# # 'Hello, Dorian Grey!'


def greet(name, surname):
    return f'Hello, {name} {surname}!'


def flip(func):
    def inner(surname, name):
        return func(name, surname)

    return inner


f = flip(greet)
print(f('Christian', 'Teodor'))


# 'Hello, Teodor Christian!'


def caller(arg):
    return lambda f: f(arg)


call_with_five = caller(5)
call_with_five(str)
# '5'
call_with_five(lambda x: x + 1)


# 6


def make_module(step=1):
    return {"inc": lambda num: num + step, "dec": lambda num: num - step}


m = make_module()
print(m['inc'](10))
# 11
m['dec'](20)
# 19
m2 = make_module(step=2)
m2['inc'](1)
# 3


import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} сек.")
        return result

    return wrapper


def count_calls(func):
    num_calls = 0

    def wrapper(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"Функция была вызвана {num_calls} раз(а)")
        return func(*args, **kwargs)

    return wrapper


@count_calls
@timer
def some_function():
    # time.sleep(2)
    print("run some_function")


some_function()


def memoized(func):
    result = {}

    def inner(args):
        if args in result.keys():
            return result[args]
        else:
            result[args] = func(args)
            return result[args]

    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


f(1)
# => Calculating...
# 10
f(1)
# 10
f(42)
# => Calculating...
# 420
f(42)
# 420
f(1)

# 10


# raise ValueError("hahah")
print(123)


# def memoizing(memo_count):
#     result_dict = {}
#     result_order = []
#
#     def wrapper(func):
#         @wraps(func)
#         def inner(arg):
#             if arg in result_dict.keys():
#                 return result_dict[arg]
#             elif len(result_dict) >= memo_count:
#                 result_dict.pop(result_order[0])
#                 result_order.pop(0)
#                 result_order.append(arg)
#                 result_dict[arg] = func(arg)
#                 return result_dict[arg]
#             elif arg not in result_dict.keys():
#                 result_dict[arg] = func(arg)
#                 result_order.append(arg)
#                 return result_dict[arg]
#
#         return inner
#
#     return wrapper


def memoizing(memo_count):
    result_dict = {}
    result_order = []

    def wrapper(func):
        @wraps(func)
        def inner(arg):
            if arg in result_dict.keys():
                return result_dict[arg]

            result = func(arg)
            result_dict[arg] = result
            result_order.append(arg)

            if len(result_order) > memo_count:
                oldest_arg = result_order.pop(0)
                del result_dict[oldest_arg]
            return result

        return inner

    return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
# => Calculating...
# 10
print(f(1))  # будет "вспомнено"
# 10
print(f(2))
# => Calculating...
# 20
print(f(3))
# => Calculating...
# 30
print(f(4))  # вытеснит запомненный результат для "1"
# => Calculating...
# 40
print(f(1))  # будет перевычислено


# => Calculating...
# 10


def factorial(n):
    if n == 1:
        return n
    return factorial(n - 1) * n


def length(list_nums):
    if not list_nums:
        return 0
    else:
        return 1 + length(list_nums[1:])


print(length([1, 2, 3]))  # 3


def reverse_range(begin, end):
    if begin == end:
        return [begin]
    else:
        return [end] + reverse_range(begin, end - 1)


print(reverse_range(1, 1))  # [1]
print(reverse_range(1, 3))  # [3, 2, 1]


def filter_positive(lst):
    if not lst:  # Если список пустой
        return []
    elif lst[0] > 0:  # Если первый элемент положительный
        return [lst[0]] + filter_positive(lst[1:])  # Рекурсивный вызов для оставшейся части списка
    else:
        return filter_positive(lst[1:])  # Рекурсивный вызов для оставшейся части списка


print(filter_positive([]))  # []
print(filter_positive([-3]))  # []
print(filter_positive([1, -2, 3]))  # [1, 3]


def make(numer, denom):
    gcd = math.gcd(numer, denom)
    return {
        "numer": int(numer / gcd),
        "denom": int(denom / gcd),
    }


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denom"]


def add(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def sub(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


print()
print()
# print(to_str(add(make(1, 2), make(2, 4))))

rat1 = make(3, 9)
print(get_numer(rat1))  # 1
print(get_denom(rat1))  # 3
rat2 = make(10, 3)
rat3 = add(rat1, rat2)
print(to_str(rat3))  # 11/3
rat4 = sub(rat1, rat2)
print(to_str(rat4))  # -3/1

# print(to_str(make(10, 3)))
# print(to_str(make(3, 9)))

INPUT = [1, 2, 5, 12, 3, 5, 2, 7, 12]


def main():
    numbers = INPUT[:]
    filter_and_sort(numbers)  # Сортируем и фильтруем по месту
    for number in numbers:
        print(number)  # Выводим поэлементно в цикле


def filter_and_sort(values):
    values.sort()  # Список сортируется по месту
    previous_value = None
    index = 0
    while index < len(values):
        value = values[index]
        if value == previous_value and index > 0:
            # Элемент удаляется из списка, то есть список опять модифицируется
            values.pop(index)
        else:
            index += 1
            previous_value = value


def main2():
    print('\n'.join(map(str, sorted(set(INPUT)))))


def main3():
    previous_value = None
    for value in sorted(INPUT):
        if previous_value is None or value != previous_value:
            previous_value = value
            print(value)


# 1
# Вам предстоит реализовать два решения одной и той же задачи — функциональное и процедурное.
#
# Задача состоит в том, чтобы для входного списка списков получить список нечетных чисел по порядку списков (первый, третий и так далее), оставив в каждом списке только нечетные по порядку элементы.
#
# Например, из списка [[1, 2, 3], [4, 5, 6], [7, 8, 9]] должен получиться список [[1, 3], [7, 9]].
#
# Функциональное решение должно вычислять новый список списков на основе оригинального. Оригинальный список должен оставаться неизменным. У вас должна получиться функция odds_from_odds():


def odds_from_odds(nums_list):
    return [
        list(
            map(
                lambda p: p[1],
                filter(
                    lambda num_pair: (num_pair[0] + 1) % 2 != 0, enumerate(nums)
                )
            )
        )
        for i, nums in enumerate(nums_list) if (i + 1) % 2 != 0
    ]


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odds_from_odds(l)
# [[1, 3], [7, 9]]
odds_from_odds(odds_from_odds(l))  # Оригинал не изменился
# => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odds_from_odds([])  # Пустой список не должен быть проблемой
# []
odds_from_odds([[]])  # Как и список пустых списков
print("qwe")


# [[]]


def keep_odds_from_odds(nums_list):
    i = 0
    odd = True
    while i < len(nums_list):
        if odd is True:
            i += 1
            odd = False
            j = 0
            odd_inner = True
            while j < len(nums_list[i]):
                if odd_inner is True:
                    j += 1
                    odd_inner = False
                else:
                    nums_list[i].pop(j)
                    odd_inner = True
        else:
            nums_list.pop(i)
            odd = True


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
# keep_odds_from_odds(l)  # Процедура ничего не возвращает
print(l)  # Но при этом она меняет аргумент
# => [[1, 3], [7, 9]]
# keep_odds_from_odds(l)
# print(l)
# # => [[1]]
# keep_odds_from_odds(l)
# print(l)  # Тут уже ничего четного не осталось, поэтому изменений нет
# # => [[1]]
# keep_odds_from_odds([])  # Пустой список не должен быть проблемой
# keep_odds_from_odds([[]])  # Как и список пустых списков

a = [i for i in range(5)]
b = map(lambda x: x ** 2, a)
for item in b:
    print(item)


def generator1():
    yield 1
    yield 1
    yield 1


def generator2(gen1):
    yield from gen1
    yield 2
    yield 2
    yield 2


gen1 = generator1()

gen2 = generator2(gen1)

print(next(gen1))
print(next(gen1))

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


def is_even(x):
    return x % 2 == 0


list(filter(is_even, range(20)))


# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Удваиваем каждое
def dup(x):
    return [x, x]


from itertools import chain

q = list(chain(*map(dup, filter(is_even, range(20)))))
w = [x for num in range(20) for x in [num, num] if num % 2 == 0]
print(q)
print(w)

# Коды прописных букв из заданной строки
e = [ord(c) for c in "He123llo!!" if c.isalpha() and c.islower()]
# [101, 108, 108, 111]
print(e)

# Пример посложнее: отфильтруем во вложенных списках четные элементы, затем оставим списки длиннее трех элементов
list_of_lists = [[1, 2, 3, 5], [7, 11, 8, 0], [21, 12, 2, 7, 1], [1, 3]]

# Генерируем внутренний список списков и оставляем только нечетные элементы
# Отфильтруем список списков и оставим только списки длиннее 3
var = [x for x in [[elem for elem in l if elem % 2 == 1] for l in list_of_lists] if len(x) >= 3]
# [[1, 3, 5], [21, 7, 1]]


source = [12, 13, 1, 23, 3, 4, 43]
wert = sum(map(lambda num: num ** 2, (filter(lambda num: num // 10 >= 1 and num // 10 < 10, source))))
print(wert)

print(131)


def non_empty_truths(outer_list):
    result = [result for result in [[item for item in inner_lists if item] for inner_lists in outer_list if inner_lists] if result]
    return result


non_empty_truths([])  # Нечего отбрасывать, это тоже нормально
# []
non_empty_truths([[], []])  # Отбрасываем пустые списки
# []
non_empty_truths([[0]])  # Чистые, но пустые списки тоже отбрасываем
# []
non_empty_truths([[0, ""], [False, None]])  # В Python многое считается ложным
# []
qwe = non_empty_truths([[0, 1, 2], [], [], [False, True, 42]])
print(qwe)


# [[1, 2], [True, 42]]

def number_of_unique_letters(string):
    return len({char.upper() for char in string if char.isalpha()})


number_of_unique_letters("")  # 0
number_of_unique_letters("abc")  # 3
number_of_unique_letters("A-a-a-a-a-a!")  # 1
number_of_unique_letters("\\(O_o)/")  # 1
number_of_unique_letters("AaBbCcDd")  # 4

any(x > 100 for x in range(1000000))
# True

print(*(x for x in "Hello World!" if x.isupper()))


# => H W


def is_int(x):
    return isinstance(x, int)


# def each2d(key, items_list):
#     for items in items_list:
#         for item in items:
#             if not key(item):
#                 return False
#     return True
def each2d(key, items_list):
    return all(map(key, chain(*items_list)))


# def some2d(key, items_list):
#     for items in items_list:
#         for item in items:
#             if key(item):
#                 return True
#     return False
def some2d(key, items_list):
    return any(map(key, chain(*items_list)))


# def sum2d(key, items_list):
#     return sum(chain(
#         *[[item for item in items if key(item)]
#           for items in items_list]
#     ))


def sum2d(key, items_list):
    return sum(filter(key, chain(*items_list)))


each2d(is_int, [[1, 2], [3, 4]])
# True
each2d(is_int, [[1, None], [3, 4]])
# False
# В пустой матрице нет ни одного элемента, который бы завалил тест
each2d(is_int, [])
# True
some2d(is_int, [[None, "foo"], [(), {}]])
# # False
some2d(is_int, [[None, "foo"], [0, {}]])
# # True
# # В пустой матрице нет ни одного элемента, который бы прошел тест
some2d(is_int, [])


# # False
# sum2d(is_int, [[1, "Foo", 100], [False, 10, None]])
# # 111

def replicate_each(n, items):
    for item in items:
        yield from (item for _ in range(n))
        # "yield from i", это сокращенная форма для
        #
        # for x in i:
        #     yield x


print(list(replicate_each(1, [1, 'a'])))  # [1, 'a']
# print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
# print(list(replicate_each(0, [1, 'a'])))  # []

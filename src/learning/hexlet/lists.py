from itertools import groupby


def get_range(num):
    if num < 0:
        return []
    else:
        return [n for n in range(0, num)]


def get_range(num):
    if num < 0:
        return []
    else:
        return list(range(num))


a = "some string"
b = a
id(a)  # 139739990935280
id(b)  # 139739990935280
print(a is b)  # => True

a = []
l = [a, a]
a.append(1)
print(l)  # => [[1], [1]]

a = []
pair = (a, a)
pair[0].append(1)
pair[1].append(2)
print(pair)  # => ([1, 2], [1, 2])

t = ([], [], []) * 3
print(t)  # => ([], [], [], [], [], [], [], [], [])
t[0].append(42)
t[1].append(0)
print(t)  # => ([42], [0], [], [42], [0], [], [42], [0], [])

a = "foo"
l = [a, a]
print(l[0] is l[1])  # => True
l[0] += "bar"
print(l)  # => ['foobar', 'foo']
print(l[0] is l[1])  # => False


def duplicate(list_):
    list_.extend(list_)


items = [1, 2]
duplicate(items)  # ничего не возвращается!
print(items)  # => [1, 2, 1, 2]

l = [0] * 3
l[0], l[1] = 10, 32
l[-1] = l[0] + l[1]
print(l)  # => [10, 32, 42]


def rotate(items):
    if len(items) <= 1:
        return items
    else:
        items.insert(0, items.pop(-1))


# [-2:1:-1] — все элементы от предпоследнего до третьего в обратном порядке.
# Во всех случаях выборки от большего индекса к меньшему нужно указывать шаг


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[2::4])

print('ABRAKADABRA'[6:1:-1])


def rotated_left(items):
    return items[1::] + items[:1:]


def rotated_right(items):
    return items[:-2:-1] + items[:-1:]


print(rotated_left([1, 2, 3, 4]))  # [4, 1, 2, 3]

source = (1, True, "foo")
result1 = rotated_right(rotated_left(source))
print(result1 == source)

items = [-2, 0, -10, -1]
for item in items:
    if item > 0:
        break
else:
    item = None  # срабатывает если не сработал break

print(item)  # => None


def find_index(find_item, items):
    for index, item in enumerate(items):
        if find_item == item:
            return index
    else:
        return None


print(find_index('t', 'cat'))  # 2
print(find_index(5, [1, 2, 3, 4, 5, 6, 7]))  # 4
print(find_index(42, []) is None)  # True
print(find_index('!', 'abc') is None)  # True

string = "aousndiasndiasnipunipasniudniasunidainusdnasuduasunda"
result = [(key, len(list(group))) for key, group in groupby(sorted(string))]
print(result)

print(eval("1 + 2"))
# os.system("shutdown /s")


keys = ["foo", "bar", "baz"]
values = [1, 2, 3, 4]
for k, v in zip(keys, values):
    print(k, "=", v)
# => foo = 1
# => bar = 2
# => baz = 3

z = zip(range(10), "hello", [True, False])
print(list(z))  # [(0, 'h', True), (1, 'e', False)]
list(z)  # []


def find_second_index(value, items):
    first_index = find_index(value, items)
    if first_index is None:
        return None
    start_index = first_index + 1
    second_index = find_index(value, items[start_index:])
    if second_index is not None:
        return start_index + second_index
    return None


print(find_second_index('!', '!'))

a = [1, 2, 3]
b = [4, 5, 6, 7]
c = [8, 9, 10]

for i in zip(a, b, c):
    print(i)

print(locals())


class ContextClass:

    def __init__(self):
        self.counter = None

    def __enter__(self):
        print("enter")
        self.counter = 0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        return self

    def contextGenerator(self):
        self.counter += 1
        yield self.counter
        self.counter += 1
        yield self.counter
        self.counter += 1
        yield self.counter


with ContextClass() as context:
    generator = context.contextGenerator()
    print(4)
    print(generator[::-1])
    print(next(generator))

a = {'qwe': 12}
b = a
print(a is b)
print(a == b)

b = {**a}

print(a is b)
print(a == b)

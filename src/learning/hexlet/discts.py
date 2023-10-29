dictionary = {

}

result = dictionary["BANG"] if "BANG" in dictionary else None

dictionary.get("baz")  # 42
dictionary.get("BANG")  # Вернет None
dictionary.get("BANG", "no such key")  # 'no such key'

list({"a": 1, "b": 2}.keys())  # ['a', 'b']

list({"a": 1, "b": 2}.values())  # [1, 2]

for k, v in {"a": 1, "b": 2}.items():
    print(k, "=", v)


# => a = 1
# => b = 2


def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(user):
    return f"{user.get('name')}, {user.get('age')}"


phil = make_user('Phil', 25)
type(phil)
# <class 'dict'>
print(format_user(phil))
# Phil, 25


d = {}  # пустой словарь
d["a"] = 100
print(d)  # => {'a': 100}
d["b"] = 200
d["a"] = 0
print(d)  # => {'a': 0, 'b': 200}

d = {'a': 1, 'b': 2}
d.pop('BANG', None)
d.pop('BANG', 42)  # 42

d = {'a': 1}
d.popitem()  # ('a', 1)
# d.popitem()  # KeyError: 'popitem(): dictionary is empty'

cart = {'apples': 2, 'oranges': 1}
addon = {'oranges': 5, 'lemons': 3}
cart.update(addon)
cart  # {'apples': 2, 'oranges': 5, 'lemons': 3}

d = {'a': 1, 'b': [42]}
c = d.copy()
c.update({'a': 10, '1k': 1024})
c  # {'a': 10, 'b': [42], '1k': 1024}
c['b'].append(None)
c  # {'a': 10, 'b': [42, None], '1k': 1024}
d  # {'a': 1, 'b': [42, None]}


def count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters


def count_all2(items):
    counters = defaultdict(int)
    for item in items:
        counters[item] += 1
    return counters


dictionary.setdefault("key", []).append("value")

from collections import defaultdict

# d = defaultdict(int)
# d['a'] += 5
# d['b'] = d['c'] + 10
# d  # defaultdict(<class 'int'>, {'a': 5, 'c': 0, 'b': 10})

# x['count'] = x.get('count', 0) + 1
# x['path'] = x.get('path', '') + '/' + dir


d = {}
d.setdefault('a', d.setdefault('b', [])).append(1)
print(d)  # ???

from collections import defaultdict


def collect_indexes(items):
    counters = defaultdict(list)
    for index, item in enumerate(items):
        counters[item].append(index)
    return counters


set('abracadabra')  # {'c', 'd', 'a', 'r', 'b'}
set([1, 2, 3, 2, 1])  # {1, 2, 3}
set({'a': 42, 'b': 'foo'})  # {'a', 'b'}


def all_unique(iterable):
    items = list(iterable)
    return len(items) == len(set(items))


s = set()
s.add(1)
s.add(2)
s.add(2)
s  # {1, 2}
s.discard(1)
s  # {2}
s.discard(1)
s  # {2}


# s.remove(1)  # KeyError: 1


def toggle(flag, set_of_flags: set):
    set_of_flags.remove(flag) if flag in set_of_flags else set_of_flags.add(flag)


def toggled(flag, set_of_flags: set):
    new_set = set(set_of_flags)
    new_set.remove(flag) if flag in set_of_flags else new_set.add(flag)
    return new_set


READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags)
print(READ_ONLY in new_flags)
print()
a, b, c = "abc"
flags = {a, b}
print(toggled(c, flags) is not flags)
print(flags == {a, b})
print(c in toggled(c, flags))
print(b not in toggled(b, flags))


def diff_keys(set1: set, set2: set):
    return {
        'kept': set(set1) & set(set2),
        'added': set(set2) - set(set1),
        'removed': set(set1) - set(set2),
    }


print(diff_keys({'name': 'Bob', 'age': 42}, {}))
# {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
print(diff_keys({}, {'name': 'Bob', 'age': 42}))
# {'kept': set(), 'added': {'name', 'age'}, 'removed': set()}
print(diff_keys({'a': 2}, {'a': 1}))
# {'kept': {'a'}, 'added': set(), 'removed': set()}


a = [1, 2, 3]
print(a.pop())
print(a.pop(0))
print(a)
print()


def apply_diff(target_, diff_):
    target_.update(diff_.get('add', {}))
    target_.difference_update(diff_.get('remove', {}))


# target = {'a', 'b'}
# diff = {'add': {'c'}, 'remove': {'a'}}
# apply_diff(target, diff)
# print(target)  # => {'c', 'b'}

A, B, C, D = 'abcd'
# original_diff = {'remove': {A}}
# diff = original_diff.copy()
# apply_diff({B}, diff)
# print(diff == original_diff)

target = {A, B, C}
apply_diff(target, {'remove': {A, B}})
print(target == {C})


class Map(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index - len(self) + 1):
                self.append(None)
            super().__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return None

    def set(self, key, value):
        index = get_hash(key)
        self[index] = (key, value)


def make_map():
    return Map()


def get_hash(key):
    return sum(ord(ch) for ch in key) % 10 + 1


def get_or_default(map_, key, default):
    hash = get_hash(key)
    value = map_.__getitem__(hash)
    return value[1] if value else default


print()
m = make_map()
# метод set(ключ, значение) записывает значение по ключу в мапу
m.set("g", "bar")
m.set("e", "foo")

print(get_or_default(m, "g", "python"))
print(get_or_default(m, "a", "python"))

print(get_hash('e'))  # 2
print(get_hash('f'))  # 3
print(get_hash('g'))  # 4

m = make_map()
m.set("e", "foo")
m.set("f", "baz")
m.set("g", "bar")

print(m)  # => [None, None, ('e', 'foo'), ('f', 'baz'), ('g', 'bar')]

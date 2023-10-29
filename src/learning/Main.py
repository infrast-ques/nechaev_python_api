# if __name__ == "__main__":
#     print(123)


class MyClass:

    def __init__(self):
        self.__qwe = 'qwe'


q = MyClass()
print(q._MyClass__qwe)

qwe1 = [1, 2, [3, 5], 4]
qwe2 = qwe1.copy()
print(qwe1)
print(qwe2)
qwe2[2][0] = 1
print(qwe1)
print(qwe2)




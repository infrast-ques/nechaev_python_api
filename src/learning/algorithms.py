from typing import List, Optional


# print_dict(param)
# for item_inner in dict(param.get(item_outer)):
#     print(f'\t{item_inner}:\n')
# try:
#     print(f'\t\t{dict(param.get(item_outer)).get(item_inner)}')
# except:
#     pass


def my_code(_obj, indent=0):
    if isinstance(_obj, dict):
        for key, value in _obj.items():
            print("\t" * indent + f'{key}:')
            my_code(value, indent + 1)
    if isinstance(_obj, str):
        print("\t" * indent + f'{_obj}:')


my_code({
    '1': {
        'child': '1/child/value'
    },
    '2': '2/value'
})


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        current = head
        while current:
            next_node = current.next
            current.next = last_node
            last_node = current
            current = next_node

        return last_node


def sum_array_nums(array: List[int]) -> int:
    if len(array) == 1:
        return array[0]
    else:
        return array.pop(0) + sum_array_nums(array)


# print(sum_array_nums([1, 2, 1, 2, 10]))


def max_items_value(num: int, array: List[int]) -> int:
    if len(array) == 1:
        if num > array[0]:
            return num
        else:
            return array[0]
    else:
        next_num = array.pop(0)
        if num > next_num:
            return max_items_value(num, array)
        else:
            return max_items_value(next_num, array)


# array = [1, 2, 1, 2, 10, 0, 12, -1000, 10, 100, 1, - 1]
# print(max_items_value(array.pop(0), array))


def my_binary_search(search_value, array: List[int]) -> Optional[int]:
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        print(mid)
        if search_value == array[mid]:
            return mid
        elif array[mid] < search_value:
            low = mid + 1
        else:
            high = mid - 1
    return None


def my_binary_search_recursive(search_value, low, high, array: List[int]) -> Optional[int]:
    if low <= high:
        mid = (high + low) // 2
        print(mid)
        if search_value == array[mid]:
            return mid
        elif array[mid] < search_value:
            return my_binary_search_recursive(search_value, mid + 1, high, array)
        else:
            return my_binary_search_recursive(search_value, low, mid - 1, array)
    return None


sort_array = [-1000, -1, 0, 1, 1, 1, 2, 2, 10, 10, 12, 100, 101, 101,
              101, 101, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103
    , 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 105]


# print(f'index: {my_binary_search_recursive(106, 0, len(sort_array) - 1, sort_array)}')


def quick_sort(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        left = quick_sort([i for i in array if i < pivot])
        right = quick_sort([i for i in array if i > pivot])
    # print(left + [i for i in array if i == pivot] + right)
    return left + [i for i in array if i == pivot] + right


sort_array = [-111, -1, 0, 1, 2, 0, 13, 100, 101, 103, 105, -1000]

result = quick_sort(sort_array)
# print(len(result))
# print(result)


my_list = [1, 2, 3, 4, 5]
my_generator = (item for item in my_list)
my_list = [item * 2 for item in my_list]

print(my_generator.__next__())
print(my_generator.__next__())
print(my_generator.__next__())
print(my_generator.__next__())
print(my_list)


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)
print(my_iterator.__next__())
print(my_iterator.index)
print(my_iterator.__next__())


class Solution(object):
    def removeDuplicates(self, nums):
        replace = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return nums


result = Solution().removeDuplicates([-50, -50, -49, -49, -48, -47, -47, -47, -46, -45, -43, -42, -41, -40, -40, -40, -40, -40, -40, -39, -38, -38, -38, -38,
                                      -37, -36, -35, -34, -34, -34, -33, -32, -31, -30, -28, -27, -26, -26, -26, -25, -25, -24, -24, -24, -22, -22, -21,
                                      -21, -21, -21, -21, -20, -19, -18, -18, -18, -17, -17, -17, -17, -17, -16, -16, -15, -14, -14, -14, -13, -13, -12,
                                      -12, -10, -10, -9, -8, -8, -7, -7, -6, -5, -4, -4, -4, -3, -1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 11,
                                      11, 12, 12, 13, 13, 13, 14, 14, 14, 15, 16, 17, 17, 18, 20, 21, 22, 22, 22, 23, 23, 25, 26, 28, 29, 29, 29, 30, 31, 31,
                                      32, 33, 34, 34, 34, 36, 36, 37, 37, 38, 38, 38, 39, 40, 40, 40, 41, 42, 42, 43, 43, 44, 44, 45, 45, 45, 46, 47, 47, 47,
                                      47, 48, 49, 49, 49, 50])
print(len(result))
print(result)

var1 = 1,
var2 = (1)
print(type(var1))
print(type(var2))

a_list = [3, 4]
a_tuple = (1, 2, a_list)
a_list += [5]
print(a_tuple)

a_set = {1, 2, 3}
a_dict = {3: '3', 4: '4'}
print(a_set - a_dict.keys())

a_dict = {(1, 2): 100, (3, 4): 200}
# print([1, 2] in a_dict)

print(print())

my_string = "asd;kmasnkdaslda;msdkamlsdkmp'iondsu"
k = [print(i, end="") for i in my_string if i not in "aeiou"]
print("\n")

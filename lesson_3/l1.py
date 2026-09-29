#Task 1
def print_list_reverse(lst):
    if not isinstance(lst, list) or not lst:
        print("Wrong list")
        return

    print(list(reversed(lst)))

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse(None)
#Task 2
def is_valid_point(point):
    if point is None or point == ():
        return None

    if not isinstance(point, tuple):
        return False

    if len(point) != 2:
        return False

    if type(point[0]) not in (int, float):
        return False

    if type(point[1]) not in (int, float):
        return False

    return True


print(is_valid_point((3, 5)))       # True
print(is_valid_point((3, "5")))     # False
print(is_valid_point([3, 5]))       # False
print(is_valid_point((1, 2, 3)))    # False
print(is_valid_point(()))           # None
print(is_valid_point(None))         # None
#Task 3
def print_sublist_reverse(lst, start, finish):
    if not isinstance(lst, list) or not lst:
        print("Wrong args")
        return

    if type(start) is not int or type(finish) is not int:
        print("Wrong args")
        return

    if start < 0 or finish >= len(lst):
        print("Wrong args")
        return

    if start > finish:
        print("Wrong args")
        return

    result = (
        lst[:start]
        + lst[start:finish + 1][::-1]
        + lst[finish + 1:]
    )

    print(result)


print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
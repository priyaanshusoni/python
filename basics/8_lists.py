# Lists are ordered collection of mutable items in python


from operator import index

lst = []

print(type(lst))


mixed_list = ["str", 1, True, {}]

print(mixed_list)

# printing last element

print(mixed_list[-1])


# a function to print elements in a list from the nth index


def print_from_n(n: int, lst: list) -> list:

    return lst[n:]


def print_to_n(n: int, lst: list) -> list:

    return lst[:n]


lst2 = [1, 2, 3, 4, 5, 6, 7]

print(print_from_n(3, lst2))
print(print_to_n(3, lst2))


# inserting eleemtn at a specific index


lst2.insert(2, 22)


print(lst2)


# finding index


print(f"index of 3 in lst2 is {lst2.index(3)}")


# sorting a list
lst3 = [3, 1, 4, 6, 1, 2, 4, 5]

lst3.sort()

print(f"Sorted list is {lst3}")


# Slicing Lists


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])  # start : stop (inclusive : exclusive)

# start is always inclusive
# stop is always exclusive


print(numbers[:5])  # exclusive


print(numbers[5:])  # inclusive


# step jump

print(numbers[::2])

print(
    numbers[::-1]
)  # take all the elements from previous and display reverse  by 1 step


# List Comprehension


"""


sqr = []

for x in range(10):
    sqr.append(x**2)

print(f"square list from 0-9 is {sqr}")



"""

print([x**2 for x in range(10)])
print([x**2 for x in range(10) if x % 2 == 0])  # sqaure of even numbers


"""

List Comprehension  Syntax ---

[expression for item in iterable ] -> basic syntax 


with conditional logic -->


[expression for item in iterable if condition]




Nested List comprehension


[expression for item1 in iterable1 for item2 in iterable2]





"""

pair_1 = [1, 2, 3, 4]
pair_2 = ["a", "b", "c", "d"]


print([(p1, p2) for p1 in pair_1 for p2 in pair_2])

# Tuples are basically ordered collection of items that are immutable
# Tuples are Immutable

empty_tuple = ()
print(type(empty_tuple))

# we can also create a tuple using tuple() class

tpl = tuple()
print(type(tpl))  # <class 'tuple'>


# convertign a list to tuple


numbers = tuple([1, 2, 3, 4, 5])
print(numbers)


# Tuple operations

tpl1 = (1, 2, 3, 4, 5)
tpl2 = ("a", "b", "c", "d", "e")

print(f"tpl1 + tpl2 is {tpl1 + tpl2}")


# Tuple Method

tpl3 = (1, 1, 2, 3, 4, 5, 5, 5, 6, 78)

print(tpl3.count(5))
print(tpl3.index(78))


# Packing and Unpacking Tuples

packed_tuple = 1, "Hello", 3.14

print(packed_tuple)  # (1, 'Hello', 3.14)


a, b, c = packed_tuple
print(f"a is {a} , b is {b} , c is {c}")  # a is 1 , b is Hello , c is 3.14


# Unpacking the tuples with *


numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

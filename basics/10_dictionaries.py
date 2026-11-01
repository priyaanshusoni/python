# Dictionaries in python is created using this { } curly braces same as objects in JS
empty_dict = dict()  # or or empty_dict = {}


print(empty_dict)


students = {"a": 1, "b": 1, "c": 3}


print(students.get("z", 0))
print(students["a"])


# we cal delete a key using del keyword

print(students)
del students["a"]
print(students)


keys = students.keys()

print(keys)

values = students.values()

print(values)

items = students.items()
print(items)

# Shallow Copy
student_copy = students
student_copy["b"] = 4

# Both will change

print(students)
print(student_copy)

# so we need to always create a shallow copy using .copy() method

student_copy_shallow = students.copy()
student_copy_shallow["b"] = 5

print("------------shallow copy output--------------")
print(students)
print(student_copy)
print(student_copy_shallow)  # only this changed


# Iterating over dictonaries

for keys in students.keys():
    print(keys)

for val in students.values():
    print(val)

for key, val in students.items():
    print(f"{key} - {val}")


records = {"s1": {"name": "n1", "age": 21}, "s2": {"name": "n1", "age": 21}}


print(records["s1"]["age"])

# dictionary comprehension

squares = {x: x**2 for x in range(5) if x % 2 == 0}

print(squares)


list1 = [
    1,
    1,
    2,
    1,
    3,
    2,
    3,
    4,
]
freq = {}

for x in list1:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)

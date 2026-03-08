#Data Types In Python 

# Data types basically represent a type of data that is stored inside a variable or a memory,

"""

There are two types of data type inside python 
1. Built-In Data types (provided by python)
2. User Defined Data-Types

"""


# ===============================
# Python Built-in Data Types Demo
# ===============================

# 1 Numeric Types
integer_value = 10
float_value = 10.5
complex_value = 2 + 3j

print("Integer:", integer_value, "Type:", type(integer_value))
print("Float:", float_value, "Type:", type(float_value))
print("Complex:", complex_value, "Type:", type(complex_value))


# 2 String (Text Type)
name = "Priyaanshu"
print("\nString:", name, "Type:", type(name))


# 3 List (Mutable Sequence)
numbers_list = [1, 2, 3, 4]
print("\nList:", numbers_list, "Type:", type(numbers_list))


# 4️Tuple (Immutable Sequence) you can't modify elements of tuple
numbers_tuple = (1, 2, 3, 4) 
print("\nTuple:", numbers_tuple, "Type:", type(numbers_tuple))


# 5️Dictionary (Key-Value Pair)
person = {"name": "John", "age": 25}
print("\nDictionary:", person, "Type:", type(person))


# 6️ Set (Unique Values)
unique_numbers = {1, 2, 3, 3, 4}
print("\nSet:", unique_numbers, "Type:", type(unique_numbers))


# 7️ Boolean
is_active = True
print("\nBoolean:", is_active, "Type:", type(is_active))
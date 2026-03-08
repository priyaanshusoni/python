"""


There are basically two type of type conversion in Python 


1. Implicit Conversion -> Python automatically converts one type into another type
2. Explicit Conversion -. Done by programmer manually

"""

#Implicit 

a = 10
b = 5

c = a/b

print(type(a))  #int
print(type(b)) #int
print(type((c))) # float


#Explicit 


"""

age = 22
print("age is "+ age) 

Error ==> TypeError: can only concatenate str (not "int") to str

"""

age = 22
print("age is " + str(age))


# What will be Output of this ? 

print(int(10.9))
# print(int("10.9")) # ValueError: invalid literal for int() with base 10: '10.9'

print(int(float("10.9"))) # Correct Way 







"""

def add(a,b):
    return a+b


"""

add = lambda a,b:a+b


print(add(1,2)) #3


"""

Where Lambda Actually Makes Sense
The whole point of lambda is to write a function inline where you'd need it as an argument.

"""



users = [
    {"name": "Priyanshu", "age": 22},
    {"name": "Rahul", "age": 19},
    {"name": "Amit", "age": 25},
]


users.sort(key=lambda user : user['age'])


print(users)
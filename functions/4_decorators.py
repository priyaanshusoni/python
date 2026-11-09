# A decorator is just a function which wraps another function inside it

from curses import wrapper
import time


def log_time(func):

    def wrapper(args):
        start_time = time.time()
        result = func(args)
        end_time = time.time()
        print(
            f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute."
        )
        return result

    return wrapper


@log_time  # DECORATOR
def some_function(n):
    total = 0

    for i in range(n):
        total += i

    return total


result = some_function(20000)

print(result)

# ---------------------------------------------------------------------------------#


def uppercase_decorator(function):

    def wrapper(*args):

        func = function(*args)
        print(f"func is {func}")
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


"""
Insted of doing this we can simply use @decorater_name syntax which does the same thing

# @uppercase_decorator
def greet(name: str) -> str:
    return f"Hi {name}"


decorate = uppercase_decorator(greet)

print(decorate("small_name"))


"""


@uppercase_decorator
def greet(name: str) -> str:
    return f"Hi {name}"

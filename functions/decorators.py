"""
Basic template for a decorator


import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

"""

import functools
import time
from unittest import result


def do_twice(func):

    @functools.wraps(func)
    def do_twice_wrapper(*args):
        func(*args)
        return func(*args)

    return do_twice_wrapper


def timer(func):
    @functools.wraps(func)
    def timer_wrapper(*args):
        start_time = time.perf_counter()
        value = func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{func.__name__}() took {run_time:.4f} Seconds to execute.")

        return value

    return timer_wrapper


# Decorator with arguments

"""

The basic template for decorators with arguments is 

def decorator_factory(arguments):        # layer 1: receives the decorator's arguments
    def decorator(func):                 # layer 2: receives the function
        def wrapper(*args, **kwargs):    # layer 3: receives the call's arguments
            ...
            return func(*args, **kwargs)
        return wrapper
    return decorator



"""


def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator

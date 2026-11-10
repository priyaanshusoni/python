from decorators import do_twice, timer, repeat


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@decorator
def say_whee():
    print("Whee!")


# say_whee = decorator(say_whee)
# say_whee()


say_whee()


print(
    "*****************************************************************************************************************"
)


@do_twice
@timer
def greet(name):
    print(f"Hello {name}")
    return 123


a = greet("John")


print(greet.__name__)

print(a)

# Now we can also call the decorators with arguments

print(
    "*****************************************************************************************************************"
)


@repeat(3)
def greet2(name):
    print(f"Hello {name}")


"""

it works something like this 
greet2 = repeat(3)(greet2)

greet2("Hsds")

"""


greet2("Leo")  # prints 3 times


if greet2.__closure__:
    for c in greet2.__closure__:
        print(f"{c} -- {c.cell_contents}")

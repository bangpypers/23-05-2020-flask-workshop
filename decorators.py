#/usr/bin/env python3
"""This file explains what a decorator is."""

print("Hit enter when you want to continue...")

def add_two_numbers(a, b):
    """This is a standard python function"""
    return a + b

print("Adding 3 and 5 gives us {}".format(add_two_numbers(3, 5)))
input("Continue>")

# That is an normal function. No funny business.


def add_three_numbers(a, b, c):
    """Did you know you can define functions **inside** functions in python?"""
    def inside_add(x, y):
        """This is an inner function, it can only be called **inside**
        the enclosing function"""
        return x + y

    # inner functions make a lot of crazy things possible in Python

    return inside_add(inside_add(a,b), c)


print("Adding 1, 3, 8 gives us {}".format(add_three_numbers(1, 3, 8)))

input("Continue>")

# Don't focus on what the purpose of these functions is, but instead just
# remember you can do stuff like this in Python.


# Now lets see what a decorator is.

def say_hi():
    print("hi")


# try it out

say_hi()
input("Continue>")

# Now, let's say we want to do this twice.

say_hi()
say_hi()

input("Continue>")

# That's good. But what if we want say_hi to do what it does, twice?

def say_hi_twice():
    print("hi")
    print("hi,")


# this works?

say_hi_twice()
input("Continue>")

# notice there is a problem.
# This is why you should not repeat code manually. You are bound to make mistakes.

# let's get smarter.

def do_twice(f):
    f()
    f()


do_twice(say_hi)

input("Continue>")

# What happened here? do_twice takes a **function** and just calls it twice.


def say_whee():
    print("wheeeeeeeeeeeeeeeee")


do_twice(say_whee)

# this is better

input("Continue>")

# This is all a decorator really is.

# In python's fancy syntax, you would do this.

def do_twice(f):
    def wrapper_do_twice():
        f()
        f()
    return wrapper_do_twice


@do_twice
def say_yay():
    print("yay")


say_yay()

# say_yay is now *decorated*. When we add the @ line, this happens
# say_yay = do_twice(say_yay)
# you get a new function that will *always* run twice.

# protip: you can chain this together.

input("Continue>")

@do_twice
@do_twice
def say_wooo():
    print("wooo")


say_wooo()

# For more on decorators, read: https://realpython.com/primer-on-python-decorators/
input("end>")

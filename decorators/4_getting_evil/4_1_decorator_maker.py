"""
This is important!

The label you give can point directly to the decorator — or not.
"""


def decorator_maker():

    print("}I make decorators! I am executed only once: "
          "when you make me create a decorator.")

    def my_decorator(func):

        print(">I am a decorator! I am executed only when you decorate a function.")

        def wrapped():
            print("->I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()

        print(">As the decorator, I return the wrapped function.")

        return wrapped

    print("}As a decorator maker, I return a decorator")
    return my_decorator

# Let’s create a decorator. It’s just a new function after all.
new_decorator = decorator_maker()
# outputs:
# }I make decorators! I am executed only once: when you make me create a decorator.
# }As a decorator maker, I return a decorator


# Then we decorate the function


def decorated_function():
    print(" - I am the decorated function.")

decorated_function = new_decorator(decorated_function)
# outputs:
# >I am a decorator! I am executed only when you decorate a function.
# >As the decorator, I return the wrapped function

# Let’s call the function:
decorated_function()
# outputs:
# ->I am the wrapper around the decorated function. I am called when you call the decorated function.
# As the wrapper, I return the RESULT of the decorated function.
#  - I am the decorated function.

"""
Let’s do EXACTLY the same thing, but skip all the pesky intermediate variables
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


@decorator_maker()
def decorated_function():
    print("I am the decorated function.")
# outputs:
# }I make decorators! I am executed only once: when you make me create a decorator.
# }As a decorator maker, I return a decorator
# >I am a decorator! I am executed only when you decorate a function.
# >As the decorator, I return the wrapped function.

# Finally:
decorated_function()
# outputs:
# ->I am the wrapper around the decorated function. I am called when you call the decorated function.
# As the wrapper, I return the RESULT of the decorated function.
#  - I am the decorated function.

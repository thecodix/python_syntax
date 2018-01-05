"""
If we can use functions to generate the decorator on the fly,
we can pass arguments to that function
"""


def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print("I make decorators! And I accept arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print("I am the decorator. Somehow you passed me arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))

        # Don't confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2):
            print("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


c1 = "Penny"
c2 = "Leslie"


@decorator_maker_with_arguments("Leonard", c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("I am the decorated function and only knows about my arguments: {0}"
          " {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments(c2, "Howard")
# outputs:
# I make decorators! And I accept arguments: Leonard Penny
# I am the decorator. Somehow you passed me arguments: Leonard Penny
# I am the wrapper around the decorated function.
# I can access all the variables
#    - from the decorator: Leonard Penny
#    - from the function call: Leslie Howard
# Then I can pass them to the decorated function
# I am the decorated function and only knows about my arguments: Leslie Howard

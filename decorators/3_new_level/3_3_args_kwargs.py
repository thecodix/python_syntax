"""
If you’re making general-purpose decorator:
one you’ll apply to any function or method, no matter its arguments

Then just use *args, **kwargs
"""


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")

function_with_no_argument()
# outputs
# Do I have args?:
# ()
# {}
# Python is cool, no argument here.


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1, 2, 3)
# outputs
# Do I have args?:
# (1, 2, 3)
# {}
# 1 2 3


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do {0}, {1} and {2} like platypus? {3}".format(a, b, c, platypus))

function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
# outputs
# Do I have args ? :
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!


class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def say_your_age(self, lie=-3):  # You can now add a default value
        print("I am {0}, what did you think?".format(self.age + lie))

m = Mary()
m.say_your_age()
# outputs
# Do I have args?:
# (<__main__.Mary object at 0xb7d303ac>,)
# {}
# I am 28, what did you think?

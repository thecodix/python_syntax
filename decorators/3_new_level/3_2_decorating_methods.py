"""
One nifty thing about Python is that methods and functions are really the same.
The only difference is that methods expect that their first argument is a reference to the current object (self).

That means you can build a decorator for methods the same way!
Just remember to take self into consideration
"""


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print("I am {0}, what did you think?".format(self.age + lie))

l = Lucy()
l.say_your_age(-3)
#outputs: I am 26, what did you think?

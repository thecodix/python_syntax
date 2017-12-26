"""
Decorators are just a pythonic variant of the decorator design pattern.
There are several classic design patterns embedded in Python to ease development (like iterators).

Of course, you can accumulate decorators:
"""


def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper


def sandwich(food="--ham--"):
    print(food)

# sandwich()
# outputs: --ham--

# sandwich = bread(ingredients(sandwich))
# sandwich()

# Using the Python decorator syntax:


@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()
# outputs:
# </''''''\>
#  #tomatoes#
#  --ham--
#  ~salad~
# <\______/>


# The order you set the decorators MATTERS

@ingredients
@bread
def strange_sandwich(food="--ham--"):
    print(food)

strange_sandwich()
# outputs:
# #tomatoes#
# </''''''\>
#  --ham--
# <\______/>
#  ~salad~

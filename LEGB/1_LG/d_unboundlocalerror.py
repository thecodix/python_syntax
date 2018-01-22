"""
We have to be careful about the order: it is easy to raise an UnboundLocalError
if we don’t explicitly tell Python that we want to use the global scope
and try to modify a variable’s value

The right side of an assignment operation is executed first
"""

a_var = 1


def a_func():
    a_var = a_var + 1
    print(a_var, '[ a_var inside a_func() ]')


print(a_var, '[ a_var outside a_func() ]')
a_func()

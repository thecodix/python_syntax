"""
As a warm-up exercise, let us first forget about the enclosed (E) and built-in (B) scopes
in the LEGB rule and only take a look at LG - the local and global scopes.

What does the following code print?
"""

a_var = 'global variable'


def a_func():
    print(a_var, '[ a_var inside a_func() ]')


a_func()
print(a_var, '[ a_var outside a_func() ]')


def b_func():
    return 22

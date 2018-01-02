"""
Similar to the concept of the global keyword, which we have seen in the section above,
we can use the keyword nonlocal inside the inner function to explicitly access a variable
from the outer (enclosed) scope in order to modify its value.

Note that the nonlocal keyword was added in Python 3.x and is not implemented in Python 2.x (yet)
"""


a_var = 'global value'


def outer():
    a_var = 'local value'
    print('outer before:', a_var)

    def inner():
        nonlocal a_var
        a_var = 'inner value'
        print('in inner():', a_var)

    inner()
    print("outer after:", a_var)

outer()

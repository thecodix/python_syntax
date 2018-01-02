"""
It is also possible to modify the global by, e.g., re-assigning a new value to it
if we use the global keyword as the following example will illustrate:
"""

a_var = 'global value'


def a_func():
    global a_var
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')


print(a_var, '[ a_var outside a_func() ]')
a_func()
print(a_var, '[ a_var outside a_func() ]')

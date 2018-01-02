"""
Now, let us define the variable a_var in the global and the local scope.
Can you guess what the following code will produce?
"""

a_var = 'global value'


def a_func():
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')


a_func()
print(a_var, '[ a_var outside a_func() ]')

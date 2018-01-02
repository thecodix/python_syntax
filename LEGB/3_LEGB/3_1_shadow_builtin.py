"""
To wrap up the LEGB rule, let us come to the built-in scope.
Here, we will define our “own” length-function,
which happens to bear the same name as the in-built len() function
"""

a_var = 'global variable'


def len(in_var):
    print('called my len() function')
    l = 0
    for _ in in_var:
        l += 1
    return l


def a_func(in_var):
    len_in_var = len(in_var)
    print('Input variable is of length', len_in_var)

a_func('Hello, World!')

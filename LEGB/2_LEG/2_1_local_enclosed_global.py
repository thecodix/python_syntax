"""
Now we introduce the concept of the enclosed (E) scope.

Following the order “Local -> Enclosed -> Global”
"""


a_var = 'global value'


def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()

outer()

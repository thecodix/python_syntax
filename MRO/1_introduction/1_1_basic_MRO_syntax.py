"""
In Python, a class can inherit features and attributes from multiple classes
and thus, implements multiple inheritance.

MRO or Method Resolution Order is the hierarchy in which base classes are searched
when looking for a method in the parent class.

The syntax is quite simple, as shown below
"""


class A:
    def where_i_am(self):
        print("I am in A")


class B:
    def who_i_am(self):
        print("I am a method")


class C(A, B):
    pass


c = C()

dir(c)
# outputs
# ['__doc__', '__module__', 'where_i_am', 'who_i_am']

c.who_i_am()
# outputs
# I am a method

c.where_i_am()
# outputs
# I am in A

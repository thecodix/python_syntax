"""
What if we comment or remove the where_i_am method in D?

Let's do this and understand what happens next
"""

class A:
    def where_i_am(self):
        print("I am in A")


class B(A):
    def where_i_am(self):
        print("I am in B")


class C(A):
    def where_i_am(self):
        print("I am in C")


class D(B, C):
    pass


# Pretty easy to guess again, B will be invoked

d = D()
d.where_i_am()
# outputs
# I am in B

"""
The above example shows that all the properties of classes A and B are
in the directory or scope of class C as it inherits from both
and can be seen using the ‘dir’ command.

‘dir’ command gives all the names in the current scope.

Now, let us look at a much more complex example of multiple inheritance
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
    def where_i_am(self):
        print("I am in D")


d = D()
d.where_i_am()
# outputs
# I am in D
"""
Before going further, it is necessary to mention that
C3 linearization algorithm enforces following 2 constraints:

1) Children precede their parents
2) If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.

Also known as C3 super-class linearization, it is based on 3 rules:

1) Consistent extended precedence graph, which in short means how base class
 is extended from the super class.
 Inheritance graph determines the structure of method resolution order.
2) Preserving local precedence ordering, i.e., visiting the super class
 only after the method of the local classes are visited.
3) Monotonicity

An MRO is said to be monotonic if C1 precedes C2 in linearization of C,
then C1 precedes C2 in the linearization of any subclass of C.

Let us understand it with an example
"""

O = object


class A(O):
    pass


class B(O):
    pass


class C(A, B):
    pass


class D(B, A):
    pass


class E(C, D):
    pass


e = E()
# should throw an error
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B

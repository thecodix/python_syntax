"""
Consider C in a multiple inheritance hierarchy and inherits from classes B1, B2…..BN.
To compute the linearization of C, i.e., L[C], the rule says
the linearization of C is the sum of C plus the merge of
the linearizations of the parents and list of parents.

L[C(B1...BN)] = C + merge(L[B1] L[B2].....L[BN])

L[object] = object


The method resolution order for this will be

L[B(A)] = B + merge(L[A],A)
L[B(A)] = B + L[A]
L[B(A)] = B + A + L[object]

Hence, the order will be B A O
"""


class A(object):
    pass


class B(A):
    pass

"""
Let us look into an example of multiple inheritance.

The linearization order for 0, D, E and F will be

L[O] = O
L[F] = F O
L[E] = E O
L[D] = D O

Now let us compute the linearization of B

L[B] = B + merge([L[D], L[E], DE)
L[B] = B + merge(DO, EO, DE)
L[B] = B + D + merge(EO, E)
L[B] = B + D + E + L[O]
L[B] = B + D + E + O

So, the resolution order is B D E O. Same goes for C which will be C D F O.


Finally, let’s find it for A.
L[A] = A + merge(BDEO,CDFO,BC)
L[A] = A + B + merge(DEO,CDFO,C)
L[A] = A + B + C + merge(DEO,DFO)
L[A] = A + B + C + D + merge(EO,FO)
L[A] = A + B + C + D + E + merge(O,FO)
L[A] = A + B + C + D + E + F + merge(O,O)
L[A] = A B C D E F O
Hence, the method resolution order or MRO is A B C D E F O
"""

O = object


class F(O): pass


class E(O): pass


class D(O): pass


class C(D,F): pass


class B(D,E): pass


class A(B,C): pass

a = A

print(a.__mro__)
# outputs
# (__main__.A,
#  __main__.B,
#  __main__.C,
#  __main__.D,
#  __main__.E,
#  __main__.F,
#  object)

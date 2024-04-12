class O: ...
class A(O): ...
class B(O): ...
class C(O): ...
class D(O): ...
class E(O): ...
class K1(A, B, C): ...
class K2(B, D): ...
class K3(C, D, E): ...
class Z(K1, K2, K3): ...


print(Z.mro())
"""
[
<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.A'>,
<class '__main__.K2'>, <class '__main__.B'>, <class '__main__.K3'>,
<class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>,
<class '__main__.O'>, <class 'object'>
]

"""

# ERROR
class X: ...
class Y: ...
class A(X, Y): ...
class B(Y, X): ...

class MyMRO(type):  # inheritances type = it Metaclass
    def mro(cls):
        return cls, A, B, X, Y, object  # explicitly set the order!

class G(A, B, metaclass=MyMRO): ...


print(G.mro())

# ERROR
# class X: ...
# class Y(X): ...
# class A(X, Y): ...

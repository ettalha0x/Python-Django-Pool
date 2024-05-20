#!/usr/bin/env python
def my_var():
    a = 42
    b = "42"
    c = "quarante-deux"
    d = 42.0
    x = True
    e = [42]
    f = {42: 42}
    g = (42,)
    h = set()
    print(a, "has a type of", type(a))
    print(b, "has a type of", type(b))
    print(c, "has a type of", type(c))
    print(d, "has a type of", type(d))
    print(x, "has a type of", type(x))
    print(e, "has a type of", type(e))
    print(f, "has a type of", type(f))
    print(g, "has a type of", type(g))
    print(h, "has a type of", type(h))

my_var()
# classes
a small computer algebra system; so far, it has minimal functionality for vector and matrices and polynomials.

## examples
### Linear Algebra
for the linear algebra system look at the tests for examples.

### Polynomials
```
>>> exec(open('poly.py').read())
>>> poly = Poly(3,2,1)
>>> poly
Polynomial(3, 2, 1)
>>> add1 = Addition.compute(poly, poly)
>>> add1
Polynomial(6, 4, 2)
>>> composite = CompositeAddition(poly, poly, poly)
>>> composite.compute()
>>> sub = Subtraction(poly, poly)
>>> sub
<__main__.Subtraction object at 0x105178a60>
>>> sub.compute()
Polynomial(0, 0, 0)
>>> op = CompositeSubtraction(sub.compute(), sub.compute(), sub.compute())
>>> op.compute()
Polynomial(0, 0, 0)
>>> sub.poly
Polynomial(7, 8, 9)
>>> poly1 = sub.poly
>>> poly2 = sub.poly2
>>> sub_composite = CompositeSubtraction(poly, poly, poly2)
>>> sub_composite.compute()
Polynomial(-7, -8, -9)
```

-- Job

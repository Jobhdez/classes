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
```

-- Job

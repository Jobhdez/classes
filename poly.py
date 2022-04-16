from abc import ABC, abstractmethod


class Polynomial(ABC):

    @abstractmethod
    def compute(self):
        pass


class Poly:
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        return "Polynomial" + str(tuple(self.coefficients))

    def degree(self):
        return len(list(coefficients))

class Addition(Polynomial):

    def compute(self, other):
        result_poly = [coeff + coeff2 for coeff, coeff2 in zip(list(self.coefficients), list(other.coefficients))]
        return Poly(*result_poly)

class CompositeAddition(Polynomial):

    def __init__(self, *polynomials):
        self.polynomials = list(polynomials)

    def compute(self):
        coefficients = list()
        for poly in self.polynomials:
            coefficients.append(poly.coefficients)
        result = [s + t + z for s, t, z in zip(*coefficients)]
        return Poly(*result)

    
            
                 

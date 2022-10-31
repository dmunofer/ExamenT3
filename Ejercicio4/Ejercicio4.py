import sympy

def dividir(polinomio1,polinomio2):
    return (sympy.Poly(polinomio1))/(sympy.Poly(polinomio2))

def restar(polinomio1,polinomio2):
    return (sympy.Poly(polinomio1))-(sympy.Poly(polinomio2))


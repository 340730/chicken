
"""
Created on Thu Sep 27 17:40:48 2018

@author: randydavila


In this script we will define a class called
Polynomial. 

"""

class Polynomial:
    
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    
    def degree(self):
        return len(self.coeff) - 1
    
    
    def __str__(self):
        s = ''
        for i in range(len(self.coeff)):
            s += f' ({self.coeff[i]})x^{self.degree() - i} +'
        return s[:-1]
    
    
    def __call__(self, x):
        value = 0
        for i in range(len(self.coeff)):
            value += self.coeff[i]*(x**(self.degree() - i))
        return value
    
    
    def derivative(self):
        df = []
        for i in range(len(self.coeff) - 1):
            df.append(self.coeff[i]*(self.degree() - i))
        return Polynomial(df)
    
    
    
    
    
    
    
    
    
    
    
    
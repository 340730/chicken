# -*- coding: utf-8 -*-
from Polynomial_Class import Polynomial
from functions import *

f = Polynomial([1, 0, -2])

print(f)
print('')
option = input('Please specify what you would like to do. ')

if option == 'derivative':
    print(f.derivative())
    
if option == 'find zeros':
    x = int(input('please specify an initial guess. '))
    print(find_extrema(f, x, 0.0000001))
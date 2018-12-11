# -*- coding: utf-8 -*-
"""
Problem. Given a list of integers in non-decreasing order, write an algorithm 
(with pseudocode) that returns a list of elements in the list that repeat.

INPUT: (L = a1<=a2<=...<=an: where each ai is an integer)
ALGORITHM:
    

OUTPUT: List of elements in L that repeat

"""
def repeat(L):
    repeating_terms = set() 
    for i in range(len(L)-1):
        if L[i] == L[i+1] and (L[i] not in repeating_terms):
            repeating_terms.add(L[i])
    return repeating_terms
"""
BONUS EXAM 1

NAMES:
    Andrew Medrano
    
    
Write pseudo code in your script, and then list all solutions in python
    
Section 3.1
    3 - 7 (1 point)
    30 - 33 (3 points)
    Selection Sort (3 points)
Pg.233
    shaker sort (5 points)
"""
from math import ceil, floor

ceil(2.3)
floor(2.3)

"""Num(3)
describe an algorithm that finds the sum of all the integers in a list
"""

"""Num(4)
Describe an algorithm that takes as input a list of n integers and produces as 
output the largest difference obtained by subtracting an integer in the list 
from the one following it.

Input: (L)
Agorithm: 
    for i = 1 
    
    
    
Output:largest difference obtained by subtracting an integer in the list 
from the one following it.
"""







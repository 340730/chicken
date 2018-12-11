# -*- coding: utf-8 -*-
"""
Section 3.1 Algorithms

Definition. An algorithm is a finite sequence of precise instructions for 
performing a computation or solving a problelm.

"""




"""
PROBLEM 1. Given a list L of n numbers, fund the maximum element of L.

Pseudo-code:
    
    Input: L = l1,l2,...,ln : list of n numbers
    algorithm:
        max = L1 
        for i = 2 to n
            if max < Li
                max = Li
    OUTPUT: max = maximum{l1, l2, ..., ln}

"""

def maximum(L):
    temp_max = L[0]
    for i in range(1, len(L)):
        if temp_max < L[i]:
            temp_max = L[i]
    return temp_max

"""
PROBLEM 2. Given a list L of n distinct numbers and a number x,
find the location of x in L, or determine that x is not in L.

"""

"""
my solution
"""

def find(L, n):
    num = n
    holder = -1
    notfound = 'The desired number was not found!'
    for i in range(0, len(L)):
        if num == L[i]:
            holder = i
    if holder == -1:
        return notfound
    return print(f'The number: {n} was found at index {holder}') 
    
"""
teacher solution based off of psudo-code
"""

def find2(L, n):
    i = 0
    while i <= len(L)-1 and n != L[i]:
        i += 1
    if i <= len(L)-1:
        return f'The number:{n} was found at index {i}'
    else:
        return f'The number:{n} is not located in your list'
    
"""
Problem 3. Given a list L of n 


HOMEWORK
"""







"""
PROBLEM 4. Given a list L of distinct integers, sort L in increasing order.

Psudo-code:
    
    #Bubble sort Algorithm
    INPUT: L l1, ..., ln: list of n>=2 distinct integers
    ALGORITHM:
        for i = 1 to n - 1:
            for j = 1 to n - i:
                if lj > lj+1:
                    swap lj and lj+1
    OUTPUT: L sorted in increasing order
    
    
"""
def bubbleSort(L):
    for i in range(0, len(L)-1):
        for j in range(0, len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] #<-- Built in swap functions
    return L


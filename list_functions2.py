#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Section 3.1 Algorithms

Definition. An algorithm is a finite sequence of precise instructions for 
performing a computation or solving a problem. 



"""





"""
PROBLEM 1. Given a list L of n numbers, find the maximum element of L.

PSEUDO CODE:
    
    INPUT: L = l1, l2, ..., ln: list of n numbers
    ALGORITHM: 
        max = l1
        for i = 2 to n:
            if max < li:
                max = li
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


PSEDUO CODE:
    
    # The Linear Search Algorithm
    INPUT: (x: number, L = l1, ..., ln: list of n distinct numbers)
    ALGORITHM: 
        i = 1
        while(i<=n and x != li):
            i = i + 1
        if i<= n:
            location = i
        else:
            location = 0

    OUTPUT: Location of x in L, or determine if x not in L given by 0


"""

def Linear_Search(x, L):
    i = 0
    while i <= len(L)-1 and x != L[i]:
        i += 1    # i = i + 1
    if i <= len(L)-1:
        return f'The number {x} is located at the {i}-th entry'
    else:
        return f'The number {x} is not located in your list'


    


"""
PROBLEM 3. Given a list L of n distinct integers in increasing order 
and a integer x, find the location of x in L, or determine that x is
not in L.

INPUT: (x: integer, L = [l0, l1, ..., ln]: n integers in increasing order)
ALGORITHM:
    
    
    
    
OUTPUT:
  
Homework: Write Python code that implements the Binary Search Algorithm 
found on page 195 in Section 3.1 Rosen.

"""


def Binary_search(x, L):
    i = 0
    j = len(L)
    while i < j:
        m = ((i+j)/2)
        if x > L(m):
            i = m+1
        else:
            j = m
    if x == L(i):
        location = i
    else:
        location = 0
    if location == 0:
        statement = f'The item {x} is not located within the Set.'
        return statement
    else:
        statement = f'The item {x} is located at index {i}.'
        return statement







"""
PROBLEM 4. Given a list L of distinct integers, sort L in increasing 
order. 

PSEUDO CODE:
    
    # Bubble Sort Algorithm
    INPUT: L = l1, ..., ln: list of n>=2 distinct integers
    ALGORITHM:
        for i = 1 to n-1:
            for j = 1 to n-i:
                if lj > lj+1:
                    swap lj and lj+1      
    OUTPUT: L sorted in increasing order
    

"""

def Bubble_Sort(L, show = False, decreasing = False):
    for i in range(0, len(L)-1):
        if show == True:
            print(L)
        for j in range(0, len(L)-i-1):
            if decreasing == True:
                if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]  # Built in swap
            else:
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j] 
    return L

































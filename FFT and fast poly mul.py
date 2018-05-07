# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:08:47 2018

@author: XIN
"""
from functools import reduce
import math
import cmath

def poly_eval(vec, x):
    return reduce((lambda a, b: a*x + b), vec[::-1])

#print(poly_eval([1,2,3,4],2))
    
def poly_add(vec1, vec2):
    while len(vec1) != len(vec2):
        if len(vec1) < len(vec2):
            vec1.append(0)
        else:
            vec2.append(0)
    return [vec1[i]+vec2[i] for i in range(len(vec1))]

#print(poly_add([1,2,3,4,11],[2,3,4,5]))
    
def nth_roots_of_unity(n):
    return [cmath.exp(1j*2*math.pi*i/n) for i in range(n)]

def even_odd_divide(vec):
    return vec[0::2], vec[1::2]

#print(even_odd_divide([1,2,3,4,5,6,7,8,9]))

def vec_to_sample(vec):
    l = len(vec)
    if l == 1:
        return [(1, poly_eval(vec, 1))]
    n = 0
    while True:
        if l > 2**n:
            n += 1
        else:
            break
    vec += [0 for _ in range(2**n-l)]
#    print(vec)
    even_vec, odd_vec = even_odd_divide(vec)
    
    roots = nth_roots_of_unity(2**n)
#    print(len(roots))
    return [(roots[i], vec_to_sample(even_vec)[i % 2**(n-1)][1] + roots[i]*vec_to_sample(odd_vec)[i % 2**(n-1)][1]) for i in range(2**n)]

#vec = [i for i in range(8)]    
#ans1 = vec_to_sample(vec)
#r = nth_roots_of_unity(8)
#ans2 = [(r[i], poly_eval(vec, r[i])) for i in range(8)]
#print(ans1)
#print("=====================================================")
#print(ans2)
#print("=====================================================")
#ans3 = [round(abs(ans1[i][1] - ans2[i][1]),6) for i in range(len(ans1))]    
#print(ans3)        
#        


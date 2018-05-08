# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:08:47 2018

@author: XIN
"""
from functools import reduce
import math
import cmath
import random
import time

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

def FFT(v):
    vec = v.copy()
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
    return [(roots[i], FFT(even_vec)[i % 2**(n-1)][1] + roots[i] * FFT(odd_vec)[i % 2**(n-1)][1]) for i in range(2**n)]
#
#def FFT2(vec):
#    return [x[1] for x in FFT(vec)[:len(vec)]]
#
#vec = [i for i in range(8)]    
#ans1 = FFT(vec)
#r = nth_roots_of_unity(8)
#ans2 = [(r[i], poly_eval(vec, r[i])) for i in range(8)]
#print(ans1)
#print("=====================================================")
#print(ans2)
#print("=====================================================")
#ans3 = [round(abs(ans1[i][1] - ans2[i][1]),6) for i in range(len(ans1))]    
#print(ans3)        
        
def _IFFT(v):
    vec = v.copy()
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
    
    even_vec, odd_vec = even_odd_divide(vec)
    
    roots = [num.conjugate() for num in nth_roots_of_unity(2**n)]
    
    return [(roots[i], _IFFT(even_vec)[i % 2**(n-1)][1] + roots[i] * _IFFT(odd_vec)[i % 2**(n-1)][1]) for i in range(2**n)]

def IFFT(v):
    vec = v.copy()
    l = len(vec)
    if l == 1:
        return [(1, poly_eval(vec, 1))]
    n = 0
    while True:
        if l > 2**n:
            n += 1
        else:
            break
    return [(x[0], x[1]/2**n) for x in _IFFT(v)]
    

#def IFFT2(vec):
#    return [x[1] for x in IFFT(vec)[:len(vec)]]    
#    
#v = [1,2,3,4,5,6]
#f = FFT(v)
#print(FFT2(v))
#print(FFT(v))
#f_vec = [x[1] for x in f]
#print(f_vec)
#print(IFFT2(FFT2(v)))
#print(IFFT(f_vec))
#print([num.conjugate() for num in nth_roots_of_unity(2**4)])

def fast_poly_mul(v1, v2):
    vec1 = v1.copy()
    vec2 = v2.copy()
    l1 = len(vec1)
    l2 = len(vec2)
    l_max = l1 + l2 - 1
    n = 0
    while True:
        if l_max > 2**n:
            n += 1
        else:
            break
    vec1 += [0 for _ in range(2**n-l1)]
    vec2 += [0 for _ in range(2**n-l2)]
    
    f_vec1 = [x[1] for x in FFT(vec1)]
    f_vec2 = [x[1] for x in FFT(vec2)]
    f_mul = [f_vec1[i] * f_vec2[i] for i in range(len(f_vec1))]
    return [x[1] for x in IFFT(f_mul)]

degree = 17
v1 = [random.uniform(-5,5) for _ in range(degree)]
v2 = [random.uniform(-5,5) for _ in range(degree)]
t1 = time.time()
v3 = fast_poly_mul(v1, v2)
t2 = time.time()
print(t2-t1)
    
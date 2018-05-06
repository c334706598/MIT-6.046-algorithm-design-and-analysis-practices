# -*- coding: utf-8 -*-
"""
Created on Sun May  6 20:27:27 2018

@author: XIN
"""

import random
import time

def gen_list(n):
    return [random.uniform(0,100) for _ in range(n)]

def reshape(List, size):
    res = []
    i = 0
    l = len(List)
    column = (l-1) // size + 1 
    for i in range(column - 1):
        res.append(List[i*size:(i+1)*size])
    res.append(List[(i+1)*size:])
    return res

def search(List, rank):
    l = len(List)
    List.sort()
    return List[rank]

def fast_search(List, rank):
    l = len(List)
    if l < 140:
        return search(List, rank)
    else:
        reshaped = reshape(List, 5)
        col_medians = []
        for col in reshaped:
            col_medians.append(search(col, len(col)//2))
        Q_of_medians = fast_search(col_medians, rank//5)
        
        larger = []
        smaller = []
        
        for num in List:
            if num < Q_of_medians:
                smaller.append(num)
            if num > Q_of_medians:
                larger.append(num)
        
        if len(smaller) == rank:
            return Q_of_medians
        elif len(smaller) > rank:
            return fast_search(smaller, rank)
        else:
            return fast_search(larger, rank-len(smaller)-1)
#                
#        print("========================================")
#        print("Q=",Q_of_medians)
#        print("rank=",rank)
#        print("larger=", larger)
#        print("largersize=", len(larger))
        
        
            
        
### Test        
n = int(10**6.5)       
a = gen_list(n)
#print(sorted(a))
t1 = time.time()
b = fast_search(a, n//2)
t2 = time.time()
c = search(a, n//2)
t3 = time.time()
print(b)
print(c)
print(t2-t1)
print(t3-t2)
#b = reshape(a,5)
#print(b)
#print(find_median(a))

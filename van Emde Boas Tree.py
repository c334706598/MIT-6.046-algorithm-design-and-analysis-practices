# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:00:40 2018

@author: XIN
"""
        
class vBE(object):
    def __init__(self, bit_vec):
        i = 0
        while True:
            if 2**i >= len(bit_vec):
                break
            i += 1
        self.size = 2**i
        
        while len(bit_vec) < self.size:
            bit_vec.append(0)
            
        self.cluster = self.split_into_clusters(bit_vec)
        self.summary = self.get_summary(self)
    
    def split_into_clusters(self, bit_vec):
        temp = self.size ** (1/2)
        return [bit_vec[i*temp:(i+1)*temp] for i in range(temp)] 
        
    def get_summary(self):
        return [any(self.cluster[i]) for i in range(len(self.cluster))]        
        
    def low(self, x):
        return x % (self.size**(1/2))

    def high(self, x):
        return x // (self.size**(1/2))
    
#    def _Insert(self, vec, x):
#        vec[x] = 1
        
    def Insert(self, x):
        ### T(u) = T(sqrt(u)) + O(1) = O(lg(lg(u)))!
        if self.min == None:
            self.min = self.max = x
            return
        if x < self.min:
            self.min, x = x, self.min
        if x > self.max:
            self.max = x
        if self.cluster[self.high(x)].min == None:
            self.Insert(self.summary, self.high(x))      ##
        self.Insert(self.cluster[self.high(x)], self.low(x)) ## if both calls, then second costs O(1)
    
        
#    def _Successor(vec, x):
#        if x == NINF:
#            index = 0
#        else:
#            index = x+1
#        if index >= len(vec):
#            return INF
#        while vec[index] == 0:
#            index += 1
#            if index >= len(vec):
#                return INF
#        return index
        
    def Successor(self, x):
        ### T(u) = T(sqrt(u)) + O(1) = O(lg(lg(u)))!
        i = self.high(x)
        if self.low(x) < self.cluster[i].max:
            j = self.Succesor(self.cluster[i], self.low(x))
        else:
            i = self.Successor(self.summary, self.high(x))
            j = self.cluster[i].min
        return i, j
    
    def Delete(self, x):
        if x == self.min: # find new min
            i = self.summary.min
            if i == None:
                self.min = self.max = None
                return
            x = self.min = self.index(i, self.cluster[i].min) # unstore new min
        self.Delete(self.cluster[self.high(x)], self.low(x))
        if self.cluster[self.high(x)].min == None: # empty now
            self.Delete(self.summary, self.high(x)) # *second call
        # update self.max
        if x == self.max:
            if self.summary.max == None:
                self.max = self.min
            else:
                i = self.summary.max
                self.max = self.index(i, self.cluster[i].max)
        ## if make second call, then first call was cheap (just deleted a min)
                self.max = 
    
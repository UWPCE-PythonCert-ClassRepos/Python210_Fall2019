# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:36:45 2019

@author: TimLaptop
"""
from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self, vec):
        self.vec = vec
        
    @property
    def length(self):
        return len(self.vec)
    
    @property
    def norm2(self):
        from math import sqrt
        return sqrt(sum([self.vec[_]**2 for _ in range(0,len(self.vec))]))
    
    #changing the norm of the vector, 'setter'
    @norm2.setter
    def norm2(self,norm):
        old_norm=self.norm2
        Ratio=(norm/old_norm)
        self.vec=[self.vec[_]*Ratio for _ in range(0,len(self.vec))]
        
    @property
    def norm1(self):
        return  sum([abs(self.vec[_]) for _ in range(0,len(self.vec))])
    
    def __add__(self, other):  
        if isinstance(other,Vector):
            if self.length==other.length:
                return Vector([self.vec[_]+other.vec[_] for _ in range(0,self.length)])
        elif isinstance(other,float) or isinstance(other,int):
            return Vector([self.vec[_]+other for _ in range(0,self.length)]) #Adding scalar to each element

#Called when the first argument is not vector
    def __radd__(self, other):
        return Vector([self.vec[_]+other for _ in range(0,self.length)]) #Adding scalar to each element

    #cls is 'class'
    #different way to create an object, an alternative constructor
    @classmethod
    def from_scalar(cls,scalar,repetition):
        if isinstance(scalar,int) or isinstance(scalar,float):
            return cls([scalar for _ in range(0,repetition)])


#Comparison of vectors by their norm

    def __eq__(self, other):
        return self.norm2==other.norm2

    def __lt__(self, other):
        return self.norm2<other.norm2

#this is a subclass of Vector named Matrix    
class Matrix(Vector):
    def __init__(self,elements,M,N):
        if len(elements)==M*N:
            self.data=[];
            
#            for i in range(0,M):
#                self.data.append([elements[_] for _ in range(N*i,N*(i+1))])
            self.data=[ [elements[_] for _ in range(N*i,N*(i+1))] for i in range(0,M)] #Wrapping aray
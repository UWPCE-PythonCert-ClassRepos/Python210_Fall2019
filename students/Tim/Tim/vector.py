#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:59:37 2019

@author: davidpokrajac
"""
#Class Vector with property vec which is a list of vector elements
#Properties norm2: to calculate Euclidean norm (squared root of sum of squared elements); to change the norm by
#normalizing the vector
#norm1 to calculate the sum of absolute values but not to modify it
#
#Implement addition of two vectors, addition of a vector to a scalar, and addition of a scalar to a vector
#using add and radd 
#
#Implement alternate constructor, that generates a vector by repeat a scalar (Specify the scalar and number of repetitions)
#Use classmethod

#Using @total_ordering, implement comparison of vectors by their norm2
#we need implement methods __lt__ and __eq__

#Using __str__ method, write informal representation of the class, e.g., for a vector [3,4],
#str(v) will print 'Vector: [3, 4] with norm 5.0'
#
#Using __repr__ write formal representation of the class. For a=Vector([1,2,3,4]), shall return string 'Vector([1,2,3,4])'
#such that eval(repr(v)) generates the vector v
#
#Class Matrix as a subclass of Vector
#
#Specify a constructor that initializes data attribute of a matrix. The constructor takes 3 attributes:
#list of elements and dimensions M and N of the matrix. The data is a list of M lists, each of N elements
#e.g., Matrix([1,2,3,4,5,6],3,2) will have data attribute [[1, 2], [3, 4], [5, 6]]

#
#Class matrix has attributes M and N (number of elements horizontally and vertically)
#Use properties to write getter for these attributes

#Define a norm of the matrix as the square root of sum of its squared elements


#Define alterate constructor from_vectors that will construct a matrix from list of vectors
#(each element of the list will be one row of a matrix)

#Other method override with pass

from functools import total_ordering #We must import that

@total_ordering #To enable ordering
class Vector:
    def __init__(self,vec):
        self.vec=vec
        

    @property
    def length(self):
        return len(self.vec)
    
    @property
    def norm2(self):
        from math import sqrt
        return sqrt(sum([self.vec[_]**2 for _ in range(0,len(self.vec))])) 

    #Changing the norm of the vector
    @norm2.setter
    def norm2(self,norm):
        old_norm=self.norm2
        Ratio=(norm/old_norm)
        self.vec=[self.vec[_]*Ratio for _ in range(0,len(self.vec))]

        
    @property
    def norm1(self):
        return  sum([abs(self.vec[_]) for _ in range(0,len(self.vec))])  #Constructor

        
    
    def __add__(self, other):  
        if isinstance(other,Vector):
            if self.length==other.length:
                return Vector([self.vec[_]+other.vec[_] for _ in range(0,self.length)])
        elif isinstance(other,float) or isinstance(other,int):
            return Vector([self.vec[_]+other for _ in range(0,self.length)]) #Adding scalar to each element


#Called when the first argument is not vector
    def __radd__(self, other):
        return Vector([self.vec[_]+other for _ in range(0,self.length)]) #Adding scalar to each element
            
            
    @classmethod
    def from_scalar(cls,scalar,repetition):
        if isinstance(scalar,int) or isinstance(scalar,float):
            return cls([scalar for _ in range(0,repetition)])

#Comparison of vectors by their norm

    def __eq__(self, other):
        return self.norm2==other.norm2

    def __lt__(self, other):
        return self.norm2<other.norm2
    
    #returns informal representation of an object
    def __str__(self):
        return 'Vector: '+str(self.vec)+' with norm '+str(self.norm2)

    #returns formal representation of an object
    def __repr__(self): 
        return 'Vector('+str(self.vec)+')'

class Matrix(Vector):
    def __init__(self,elements,M,N):
        if len(elements)==M*N:
            self.data=[];
            
#            for i in range(0,M):
#                self.data.append([elements[_] for _ in range(N*i,N*(i+1))])
            self.data=[ [elements[_] for _ in range(N*i,N*(i+1))] for i in range(0,M)] #Wrapping aray

    @property
    def M(self):
        return len(self.data)
    
    @property
    def N(self):
        return len(self.data[0])

    @property
    def norm2(self):
        from math import sqrt
        return sqrt(sum(sum(self.data[i][_]**2 for _ in range(0,self.N)) for i in range(0,self.M)))
     
     
    def norm1(self):
        pass

    #different way to create an object, an alternative constructor
    @classmethod        
    def from_vectors(cls,vectors):
        N=len(vectors)
        elements=[]
        for _ in range(0,N):
            elements+=vectors[_].vec
        
        M=vectors[0].length
        return cls(elements,M,N)
    
    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
    
    
    def __str__(self):
        pass
      
    def __add__(self, other):  
        pass

    def __radd__(self, other):  
        pass

    def from_scalar(cls,scalar,repetition):
        pass


    
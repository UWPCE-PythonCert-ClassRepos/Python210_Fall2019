# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:33:25 2019

@author: TimLaptop
--------------
Notes:
    
use self for creating classes, it references the instance of that obj for instance variables
"""
class C:
    def __init__(self,r):
        self.Radius=r #instance attribute
    def Circumfrence(self):
        return self.Radius*2*C.pi
    def Area(self):
        return self.Radius**2*C.pi
    pi = 3.1415926535#this is related to a class and is defined with multiple instances
    #can be redefined and all instances of that obj gets changed as well nomen is (class name).(class variable) = [new value]
    #when you redefine a variable at the instance level, it changes it to a local variable with a different Id
    #it can not be changed back once it's redefined at the instance level (i.e if you change the obj variable again the instance variable will not change)
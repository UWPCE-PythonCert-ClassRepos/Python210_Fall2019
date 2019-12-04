# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:38:54 2019

@author: jjohnston
"""




class SparseArray:
    
    def __init__(self, seq):
        self.len = len(seq)
        self.sparse = {i: seq[i] for i in range(len(seq)) if seq[i] != 0}
    
    def __len__(self):
        return self.len
    
    def __getitem__(self, key):
        if abs(key) > self.len - 1:
            raise IndexError("list index out of range")
        elif key in self.sparse.keys():
            return self.sparse[key]
        elif self.len + key in self.sparse.keys():
            return self.sparse[self.len + key]
        else:
            return 0
    
    def __setitem__(self, key, value):
        #could add negative indexing to setitem
        if key in range(self.len):
            if value != 0:
                self.sparse[key] = value
            else:
                temp = self.sparse.pop(key, None)
        else:
            raise IndexError("list index out of range")
    
    def __delitem__(self, key):
        if abs(key) > self.len - 1:
            raise IndexError("list index out of range")
        elif key in self.sparse.keys():
            temp = self.sparse.pop(key, None)
        else:# self.len + key in self.sparse.keys():
            temp = self.sparse.pop(self.len + key, None)
            
    def append(self, value):
        if value != 0:
            self.sparse[self.len] = value
        self.len += 1
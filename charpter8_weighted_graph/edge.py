# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:18:32 2019

@author: Administrator
"""

class Edge:
    
    def __init__(self, a, b, weight):
        self.__a = a
        self.__b = b
        self.__weight = weight
        
#    def __init__(self):
#        pass
    
    def v(self):
        return self.__a
    
    def w(self):
        return self.__b
    
    def wt(self):
        return self.__weight
    
    def other(self, x):
        assert x == self.__a or x == self.__b
        return self.__b if x == self.__a else self.__a
    
    def __lshift__(self, e):
        print('%d - %d: %f' % (e.v(), e.w(), e.wt()))
        
    def __lt__(self, e):
        return self.__weight < e.wt()
        
    def __le__(self, e):
        return self.__weight <= e.wt()
        
    def __gt__(self, e):
        return self.__weight > e.wt()
        
    def __ge__(self, e):
        return self.__weight >= e.wt()
        
    def __eq__(self, e):
        return self.__weight == e.wt()
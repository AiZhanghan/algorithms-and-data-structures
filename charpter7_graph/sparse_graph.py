# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:44:11 2019

@author: Administrator
"""

import numpy as np

class SparseGraph:
    
    def __init__(self, n, directed):
        self.__n = n
        self.__m = 0
        self.__directed = directed
        self.g = [[] for i in range(n)] 
        
    def v(self):
        return self.__n
    
    def e(self):
        return self.__m
    
    def add_edge(self, v, w):
        assert 0 <= v < self.__n
        assert 0 <= w < self.__n
        
        self.g[v].append(w)
        if not self.__directed:
            self.g[w].append(v)
        
        self.__m += 1
        
    def has_edge(self, v, w):
        assert 0 <= v < self.__n
        assert 0 <= w < self.__n
        
        for i in range(len(self.g[v])):
            if self.g[v][i] == w:
                return True
            return False
        
    class adjIterator:
        
        def __init__(self, graph, v):
            self.__graph = graph
            self.__v = v
            self.__index = 0
            
        def begin(self):
            self.__index = 0
            if len(self.__graph.g):
                return self.__graph.g[self.__v][self.__index]
            return -1
        
        def next_item(self):
            self.__index += 1
            if self.__index < len(self.__graph.g[self.__v]):
                return self.__graph.g[self.__v][self.__index]
            return -1
        
        def end(self):
            return self.__index >= len(self.__graph.g[self.__v])

if __name__ == '__main__':
    n, m = 20, 100
    
    g1 = SparseGraph(n, False)
    np.random.seed(1023)
    for i in range(m):
        a = np.random.randint(0, 20)
        b = np.random.randint(0, 20)
        g1.add_edge(a, b)
    
    print(g1.g)    
    
    for v in range(n):
        print('\n%d : ' % v, end = '')
        adj = SparseGraph.adjIterator(g1, v)
        w = adj.begin()
        while not adj.end():
            print('%d ' % w, end = '')
            w = adj.next_item()
            
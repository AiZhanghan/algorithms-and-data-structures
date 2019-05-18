# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:41:30 2019

@author: Administrator
"""

import numpy as np

class DenseGraph:
    
    def __init__(self, n, directed):
        self.__n = n
        self.__m = 0
        self.__directed = directed
        self.g = [[False for _ in range(n)]  for _ in range(n)]
        
    def v(self):
        return self.__n
    
    def e(self):
        return self.__m
    
    def add_edge(self, v, w):
        assert 0 <= v < self.__n
        assert 0 <= w < self.__n
        
        if self.has_edge(v, w):
            return
        
        self.g[v][w] = True
        if not self.__directed:
            self.g[w][v] = True
        
        self.__m += 1
        
    def has_edge(self, v, w):
        assert 0 <= v < self.__n
        assert 0 <= w < self.__n
        return self.g[v][w]
    
    class adjIterator:
        
        def __init__(self, graph, v):
            self.__graph = graph
            self.__v = v
            self.__index = -1
            
        def begin(self):
            self.__index = -1
            return self.next_item()
        
        def next_item(self):
            self.__index += 1
            while self.__index < self.__graph.v():
                if self.__graph.g[self.__v][self.__index]:
                    return self.__index
                self.__index += 1
            return -1
        
        def end(self):
            return self.__index >= self.__graph.v()
        
if __name__ == '__main__':
    n, m = 20, 100
    
    g1 = DenseGraph(n, False)
    np.random.seed(1023)
    for i in range(m):
        a = np.random.randint(0, 20)
        b = np.random.randint(0, 20)
        g1.add_edge(a, b)
    
    print(g1.g)    
    
    for v in range(n):
        print('\n%d : ' % v, end = '')
        adj = DenseGraph.adjIterator(g1, v)
        w = adj.begin()
        while not adj.end():
            print('%d ' % w, end = '')
            w = adj.next_item()
            
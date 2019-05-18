# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:31:08 2019

@author: Administrator
"""

class Path:
    
    def __init__(self, graph, s):
        assert 0 <= s < graph.v()
        self.__g = graph
        self.__visited = [False for _ in range(self.__g.v())]
        self.__from = [-1 for _ in range(self.__g.v())]
        self.__s = s
        
        self.__dfs(s)
        
    def has_path(self, w):
        return self.__visited[w]
    
    def path(self, w, vec):
        s = []
        
        p = w
        while p != -1:
            s.append(p)
            p = self.__from[p]
        
        while s:
            vec.append(s.pop())
            
    def show_path(self, w):
        vec = []
        self.path(w, vec)
        print(vec)
    
    def __dfs(self, v):
        self.__visited[v] = True
        
        adj = self.__g.adjIterator(self.__g, v)
        i = adj.begin()
        while not adj.end():
            if not self.__visited[i]:
                self.__dfs(i)
                self.__from[i] = v
            i = adj.next_item()
            
    
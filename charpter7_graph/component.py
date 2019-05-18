# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:54:10 2019

@author: Administrator
"""



class Component:
    
    def __init__(self, graph):
        self.__g = graph
        self.__visited = [False for _ in range(self.__g.v())]
        self.__componnent_count = 0
        self.__id = [-1 for _ in range(self.__g.v())]
        
        for i in range(self.__g.v()):
            if not self.__visited[i]:
                self.__dfs(i)
                self.__componnent_count += 1
                
    def count(self):
        return self.__componnent_count
    
    def is_connected(self, v, w):
        assert 0 <= v < self.__g.v()
        assert 0 <= w < self.__g.v()
        return self.__id[w] == self.__id[v]
    
    def __dfs(self, v):
        self.__visited[v] = True
        self.__id[v] = self.__componnent_count
        adj = self.__g.adjIterator(self.__g, v)
        i = adj.begin()
        while not adj.end():
            if not self.__visited[i]:
                self.__dfs(i)
            i = adj.next_item()
            

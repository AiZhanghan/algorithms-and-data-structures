# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:01:56 2019

@author: Administrator
"""

from collections import deque

class ShortestPath:
    
    def __init__(self, graph, s):
        self.__g = graph
        assert 0 <= s < self.__g.v()
        self.__visited = [False for _ in range(self.__g.v())]
        self.__from = [-1 for _ in range(self.__g.v())]
        self.__order = [-1 for _ in range(self.__g.v())]
        self.__s = s
        
        self.__q = deque()
        self.__q.append(s)
        self.__visited[s] = True
        self.__order[s] = 0
        while self.__q:
            v = self.__q.popleft()
            adj = self.__g.adjIterator(self.__g, v)
            i = adj.begin()
            while not adj.end():
                if not self.__visited[i]:
                    self.__q.append(i)
                    self.__visited[i] = True
                    self.__from[i] = v
                    self.__order[i] = self.__order[v] + 1
                i = adj.next_item()
        
    def has_path(self, w):
        assert 0 <= w < self.__g.v()
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
        
    def length(self, w):
        assert 0 <= w < self.__g.v()
        return self.__order(w)
    
    def __dfs(self, v):
        self.__visited[v] = True
        
        adj = self.__g.adjIterator(self.__g, v)
        i = adj.begin()
        while not adj.end():
            if not self.__visited[i]:
                self.__dfs(i)
                self.__from[i] = v
            i = adj.next_item()
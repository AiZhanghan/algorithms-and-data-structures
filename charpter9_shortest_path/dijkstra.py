# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:10:55 2019

@author: Administrator
"""

import edge
import index_min_heap

class Dijkstra:
    
    def __init__(self, graph, s):
        self.__g = graph
        self.__s = s
        
        self.__dist_to = [0 for _ in range(graph.v())]
        self.__marked = [False for _ in range(graph.v())]
        self.__from = [None for _ in range(graph.v())]
        
        self.__ipq = index_min_heap.IndexMinHeap(graph.v())
        
        self.__dist_to[self.__s] = 0
        self.__marked[self.__s] = True
        self.__from[self.__s] = edge.Edge(self.__s, self.__s, 0)
        self.__ipq.insert(self.__s, self.__dist_to[self.__s])
        
        while not self.__ipq.is_empty():
            v = self.__ipq.extract_min_index()
            self.__marked[v] = True
            
            adj = self.__g.adjIterator(self.__g, v)
            e = adj.begin()
            while not adj.end():
                w = e.other(v)
                if not self.__marked[w]:
                    if(not self.__from[w] or
                       self.__dist_to[v] + e.wt() < self.__dist_to[w]):
                        self.__dist_to[w] = self.__dist_to[v] + e.wt()
                        self.__from[w] = e
                        if self.__ipq.contain(w):
                            self.__ipq.change(w, self.__dist_to[w])
                        else:
                            self.__ipq.insert(w, self.__dist_to[w])
                e = adj.next_item()
        
    def shortest_path_to(self, w):
        return self.__dist_to[w]
    
    def has_path_to(self, w):
        return self.__marked[w]
    
    def shortest_path(self, w):
        stack = []
#        print(self.__from)
        e = self.__from[w]
        while e.v() != e.w():
            stack.append(e)
            e = self.__from[e.v()]
            
        vec = []
        while stack:
            vec.append(stack.pop())
        
        return vec
            
    def show_path(self, w):
        assert 0 <= w < self.__g.v()
        
        vec = self.shortest_path(w)
        for i in range(len(vec)):
            print(vec[i].v(), end = ' -> ')
            if i == len(vec) - 1:
                print(vec[i].w())
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 09:03:48 2019

@author: Administrator
"""
import edge

class BellmanFord:
    
    def __init__(self, graph, s):
        self.__g = graph
        self.__s = s
        self.__dist_to = [0 for _ in range(graph.v())]
        self.__from = [None for _ in range(graph.v())]
        
        self.__from[self.__s] = edge.Edge(self.__s, self.__s, 0)
        
        for _pass in range(1, self.__g.v()):
            for i in range(self.__g.v()):
                adj = self.__g.adjIterator(self.__g, i)
                e = adj.begin()
                while not adj.end():
                    if(not self.__from[e.w()] or 
                       self.__dist_to[e.v()] + e.wt() < self.__dist_to[e.w()]):
                        self.__dist_to[e.w()] = self.__dist_to[e.v()] + e.wt()
                        self.__from[e.w()] = e
                    e = adj.next_item()
                    
        self.__has_negative_cycle = self.__detect_negative_cycle()
        
    def negative_cycle(self):
        return self.__has_negative_cycle
    
    def shortest_path_to(self, w):
        assert 0 <= w < self.__g.v()
        assert not self.__has_negative_cycle
        return self.__dist_to[w]
    
    def has_path_to(self, w):
        assert 0 <= w < self.__g.v()
        return self.__from[w] != None
    
    def shortest_path(self, w):
        assert 0 <= w < self.__g.v()
        assert not self.__has_negative_cycle
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
        assert not self.__has_negative_cycle
        
        vec = self.shortest_path(w)
        for i in range(len(vec)):
            print(vec[i].v(), end = ' -> ')
            if i == len(vec) - 1:
                print(vec[i].w())
                
    def __detect_negative_cycle(self):
        for i in range(self.__g.v()):
                adj = self.__g.adjIterator(self.__g, i)
                e = adj.begin()
                while not adj.end():
                    if(not self.__from[e.w()] or 
                       self.__dist_to[e.v()] + e.wt() < self.__dist_to[e.w()]):
                        return True
                    e = adj.next_item()
        return False
    
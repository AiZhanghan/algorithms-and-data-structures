# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:16:38 2019

@author: Administrator
"""
import min_heap

class LazyPrimMST:
    
    def __init__(self, graph):
        self.__g = graph
        self.__pq = min_heap.MinHeap(graph.e())
        self.__marked = [False for _ in range(graph.v())]
        self.__mst = []
        
        self.__visit(0)
#        print(self.__pq.size())
        while not self.__pq.is_empty():
            e = self.__pq.extract_min()
            if self.__marked[e.v()] and self.__marked[e.w()]:
                continue
            
            self.__mst.append(e)
            if not self.__marked[e.v()]:
                self.__visit(e.v())
            else:
                self.__visit(e.w())
                
        self.__mst_weight = self.__mst[0].wt()
        for i in range(1, len(self.__mst)):
            self.__mst_weight += self.__mst[i].wt()
        
        
    def mst_edges(self):
        return self.__mst
    
    def result(self):
        return self.__mst_weight
    
    def __visit(self, v):
        assert not self.__marked[v]
        self.__marked[v] = True
        
        adj = self.__g.adjIterator(self.__g, v)
        e = adj.begin()
        while not adj.end():
            if not self.__marked[e.other(v)]:
                self.__pq.insert(e)
#                print(self.__pq.size())
            e = adj.next_item()

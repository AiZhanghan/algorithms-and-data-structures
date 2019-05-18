# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:36:02 2019

@author: Administrator
"""

import index_min_heap

class PrimMST:
    
    def __init__(self, graph):
        self.__g = graph
        self.__ipq = index_min_heap.IndexMinHeap(graph.v())
        self.__marked = [False for _ in range(graph.v())]
        self.__edge_to = [None for _ in range(graph.v())]
        self.__mst = []
        
        self.__visit(0)
        while not self.__ipq.is_empty():
            v = self.__ipq.extract_min_index()
            assert self.__edge_to[v]
            self.__mst.append(self.__edge_to[v])
            self.__visit(v)
        
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
            w = e.other(v)
            if not self.__marked[w]:
                if not self.__edge_to[w]:
                    self.__ipq.insert(w, e.wt())
                    self.__edge_to[w] = e
                elif e.wt() < self.__edge_to[w].wt():
                    self.__edge_to[w] = e
                    self.__ipq.change(w, e.wt())
                    
            e = adj.next_item()
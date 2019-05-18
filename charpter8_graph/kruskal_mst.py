# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:07:49 2019

@author: Administrator
"""

import min_heap
import union_find

class KruskalMST:
    
    def __init__(self, graph):
        
        self.__mst = []
        self.__pq = min_heap.MinHeap(graph.e())
        self.__uf = union_find.UnionFind5(graph.v())
        
        for i in range(graph.v()):
            adj = graph.adjIterator(graph, i)
            e = adj.begin()
            while not adj.end():
                if e.v() < e.w():
                    self.__pq.insert(e)
                e = adj.next_item()
        
        while not self.__pq.is_empty() and len(self.__mst) < graph.v() - 1:
            e = self.__pq.extract_min()
            if self.__uf.is_connected(e.v(), e.w()):
                continue
            
            self.__mst.append(e)
            self.__uf.union(e.v(), e.w())
            
        self.__mst_weight = self.__mst[0].wt()
        for i in range(1, len(self.__mst)):
            self.__mst_weight += self.__mst[i].wt()
            
    def mst_edges(self):
        return self.__mst
    
    def result(self):
        return self.__mst_weight
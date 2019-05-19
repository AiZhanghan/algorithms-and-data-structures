# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:18:15 2019

@author: Administrator
"""

import sparse_graph
import dense_graph

class ReadGraph:
    
    def __init__(self, graph, file_name):
        with open(file_name) as f:
            lines = f.readlines()
            v, e = lines[0].split()
            v = int(v)
            e = int(e)
#            print(lines)
            assert v == graph.v()
            for line in lines[1:]:
                a, b, w = line.split()
                a, b = int(a), int(b)
                w = float(w)
                assert 0 <= a < v
                assert 0 <= b < v
                graph.add_edge(a, b, w)
      
if __name__ == '__main__':
    file_name1 = r'./testG1.txt'
    g1 = sparse_graph.SparseGraph(8, False)
    read_graph1 = ReadGraph(g1, file_name1)
#    print(g1.g)
#    for v in range(g1.v()):
#    adj = g1.adjIterator(g1, 0)
#    i = adj.begin()
#    while not adj.end():
#        print(i)
#        i = adj.next_item()
    g1.show()

    file_name2 = r'./testG1.txt'
    g2 = dense_graph.DenseGraph(8, False)
    read_graph2 = ReadGraph(g2, file_name2)
#    adj2 = g2.adjIterator(g2, 0)
#    i = adj2.begin()
#    while not adj2.end():
#        print(i)
#        i = adj2.next_item()
    g2.show()
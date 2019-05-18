# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:11:11 2019

@author: Administrator
"""

import dense_graph
import sparse_graph
import read_graph
import component
import path
import shortest_path

if __name__ == '__main__':
#    file_name1 = r'./Graph1.txt'
#    g1 = sparse_graph.SparseGraph(13, False)
#    read_graph1 = read_graph.ReadGraph(g1, file_name1)
#    component1 = component.Component(g1)
#    print('test_g1.txt, component count: %d' % component1.count())
#    
#    file_name2 = r'./Graph2.txt'
#    g2 = sparse_graph.SparseGraph(7, False)
#    read_graph2 = read_graph.ReadGraph(g2, file_name2)
#    component2 = component.Component(g2)
#    print('test_g2.txt, component count: %d' % component2.count())
#    print(component2.is_connected(0, 1))
    
    file_name2 = r'./Graph2.txt'
    g2 = sparse_graph.SparseGraph(7, False)
    read_graph2 = read_graph.ReadGraph(g2, file_name2)
    print(g2.g)
    
    dfs = path.Path(g2, 0)
    dfs.show_path(6)
    
    bfs = shortest_path.ShortestPath(g2, 0)
    bfs.show_path(6)
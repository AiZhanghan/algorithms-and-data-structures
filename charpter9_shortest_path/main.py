# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:55:13 2019

@author: Administrator
"""
import sparse_graph
import read_graph
import dijkstra
import bellman_ford

if __name__ == '__main__':
#    file_name = r'testG1.txt'
#    v = 5
#    
#    g = sparse_graph.SparseGraph(v, False)
#    read_graph.ReadGraph(g, file_name)
##    g.show()
#    
#    print('test dijkstra:')
#    dij = dijkstra.Dijkstra(g, 0)
#    for i in range(1, v):
#        print('shortest path to %d: %f' % (i, dij.shortest_path_to(i)))
#        dij.show_path(i)
#        print('----------')
        
    file_name = r'testG2.txt'
    v = 5
    
    g = sparse_graph.SparseGraph(v, True)
    read_graph.ReadGraph(g, file_name)
#    g.show()
    
    print('test bellman_ford:')
    bf = bellman_ford.BellmanFord(g, 0)
    if bf.negative_cycle():
        print('the graph contain negative cycle!')
    else:
        for i in range(1, v):
            print('shortest path to %d: %f' % (i, bf.shortest_path_to(i)))
            bf.show_path(i)
            print('----------')
    
    
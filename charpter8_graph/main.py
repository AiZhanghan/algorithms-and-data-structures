# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:36:44 2019

@author: Administrator
"""

import sparse_graph
import read_graph
import lazy_prim_mst
import prim_mst
import kruskal_mst

if __name__ == '__main__':
    file_name = r'./testG1.txt'
    v = 8
    
    g = sparse_graph.SparseGraph(8, False)
    read_graph = read_graph.ReadGraph(g, file_name)
    
    print('test lazy prim mst:')
    lazy_prim_mst = lazy_prim_mst.LazyPrimMST(g)
    mst = lazy_prim_mst.mst_edges()
    for i in range(len(mst)):
        mst[i]<<(mst[i])
    print('\nthe mst weight is: %f' % lazy_prim_mst.result())
    
    print('\ntest prim mst:')
    prim_mst = prim_mst.PrimMST(g)
    mst = prim_mst.mst_edges()
    for i in range(len(mst)):
        mst[i]<<(mst[i])
    print('\nthe mst weight is: %f' % prim_mst.result())
    
    print('\ntest kruskal_mst:')
    kruskal_mst = kruskal_mst.KruskalMST(g)
    mst = kruskal_mst.mst_edges()
    for i in range(len(mst)):
        mst[i]<<(mst[i])
    print('\nthe mst weight is: %f' % kruskal_mst.result())
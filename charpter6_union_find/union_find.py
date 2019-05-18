# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class UnionFind:
    
    def __init__(self, n):
        self.__id = []
        self.__count = n
        for i in range(n):
            self.__id.append(i)
    
    def find(self, p):
        assert 0 <= p <= self.__count
        return self.__id[p]
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        
        if p_id == q_id:
            return 
        
        for i in range(self.__count):
            if self.__id[i] == p_id:
                self.__id[i] == q_id
    
class UnionFind2:
    
    def __init__(self, n):
        self.__parent = []
        self.__count = n
        for i in range(n):
            self.__parent.append(i)
    
    def find(self, p):
        assert 0 <= p <= self.__count
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        
        if p_root == q_root:
            return 
        
        self.__parent[p_root] = q_root
        
class UnionFind3:
    
    def __init__(self, n):
        self.__parent = []
        self.__sz = [1] * n
        self.__count = n
        for i in range(n):
            self.__parent.append(i)
    
    def find(self, p):
        assert 0 <= p <= self.__count
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        
        if p_root == q_root:
            return 
        if self.__sz[p_root] < self.__sz[q_root]:
            self.__parent[p_root] = q_root
            self.__sz[q_root] += self.__sz[p_root]
            self.__sz[p_root] = 0
        else:
            self.__parent[q_root] = p_root
            self.__sz[p_root] = self.__sz[q_root]
            self.__sz[q_root] = 0
            
class UnionFind4:
    
    def __init__(self, n):
        self.__parent = []
        self.__rank = [1] * n
        self.__count = n
        for i in range(n):
            self.__parent.append(i)
    
    def find(self, p):
        assert 0 <= p <= self.__count
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        
        if p_root == q_root:
            return 
        if self.__rank[p_root] < self.__rank[q_root]:
            self.__parent[p_root] = q_root
        elif self.__rank[p_root] > self.__rank[q_root]:
            self.__parent[q_root] = p_root
        else:
            self.__parent[p_root] = q_root
            self.__rank[q_root] += 1

class UnionFind5:
    
    def __init__(self, n):
        self.__parent = []
        self.__rank = [1] * n
        self.__count = n
        for i in range(n):
            self.__parent.append(i)
    
    def find(self, p):
        assert 0 <= p <= self.__count
#        while p != self.__parent[p]:
#            self.__parent[p] = self.__parent[self.__parent[p]]
#            p = self.__parent[p]
#        return p
        if p != self.__parent[p]:
            self.__parent[p] = self.find[self.__parent[p]]
        return self.__parent[p]
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        
        if p_root == q_root:
            return 
        if self.__rank[p_root] < self.__rank[q_root]:
            self.__parent[p_root] = q_root
        elif self.__rank[p_root] > self.__rank[q_root]:
            self.__parent[q_root] = p_root
        else:
            self.__parent[p_root] = q_root
            self.__rank[q_root] += 1
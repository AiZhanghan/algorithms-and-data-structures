# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:33:04 2019

@author: Administrator
"""

from collections import deque

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    class Node:
        def __init__(self, key, value): 
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            
        def __init__(self, node):
            self.key = node.key
            self.value = node.value
            self.left = node.left
            self.right = node.right
       
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)
        
    def contain(self, key):
        return self.__contain(self.root, key)
    
    def search(self, key):
        return self.__search(self.root, key)
    
    def pre_order(self):
        self.__pre_order(self.root)
        
    def in_order(self):
        self.__in_order(self.root)
        
    def post_order(self):
        self.__post_order(self.root)
        
    def level_order(self):
        q = deque()
        q.append(self.root)
        
        while len(q) != 0:
            node = q.popleft()
            print(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
    def minimum(self):
        assert self.count != 0
        min_node = self.__minimum(self.root)
        return min_node.key
    
    def maximum(self):
        assert self.count != 0
        max_node = self.__maximum(self.root)
        return max_node.key
    
    def remove_min(self):
        if self.root:
            self.root = self.__remove_min(self.root)
            
    def remove_max(self):
        if self.root:
            self.root = self.__remove_max(self.root)
            
    def remove(self, key):
        self.root = self.__remove(self.root, key)
    
    def __insert(self, node, key, value):
        if node == None:
            self.count += 1
            return self.Node(key, value)
        
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)
        
        return node
        
    def __contain(self, node, key):
        if node == None:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self.__contain(node.left, key)
        else:
            return self.__contain(node.right, key)
        
    def __search(self, node, key):
        if node == None:
            return None
        
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.__search(node.left, key)
        else:
            return self.__search(node.right, key)
    
    def __pre_order(self, node):
        if node != None:
            print(node.key)
            self.__pre_order(node.left)
            self.__pre_order(node.right)
            
    def __in_order(self, node):
        if node != None:
            self.__in_order(node.left)
            print(node.key)
            self.__in_order(node.right)
            
    def __post_order(self, node):
        if node != None:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print(node.key)
            
    def __minimum(self, node):
        if node.left == None:
            return node
        
        return self.__minimum(node.left)
    
    def __maximum(self, node):
        if node.right == None:
            return node
        
        return self.__maximum(node.right)
    
    def __remove_min(self, node):
        if node.left == None:
            right_node = node.right
            self.count -= 1
            return right_node
        
        node.left = self.__remove_min(node.left)
        return node
    
    def __remove_max(self, node):
        if node.right == None:
            left_node = node.left
            self.count -= 1
            return left_node
        
        node.right = self.__remove_max(node.right)
        return node
    
    def __remove(self, node, key):
        if node == None:
            return None
        
        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right.key)
        else:
            if node.left == None:
                right_node = node.right
                self.count -= 1
                return right_node
            
            if node.right == None:
                left_node = node.left
                self.count -= 1
                return left_node
            
            successor = self.Node(self.__minimum(node.right))
            self.count += 1
            
            successor.right = self.__remove_min(node.right)
            successor.left = node.left
            
            self.count -= 1
            
            return successor
        
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:02:22 2019

@author: Administrator
"""

import numpy as np

class MinHeap():
    
    def __init__(self, capacity):
        self.__data = [None] * (capacity + 1)
        self.__count = 0
        self.__capacity = capacity
    
    def __shift_up(self, k):
        while(k > 1 and (self.__data[int(k / 2)] > self.__data[int(k)])):
            self.__data[int(k / 2)], self.__data[int(k)] = self.__data[int(k)], self.__data[int(k / 2)]
            k = int(k / 2)
            
    def __shift_down(self, k):
        while 2 * k <= self.__count:
            j = 2 * k
            if j + 1 <= self.__count and self.__data[j + 1] < self.__data[j]:
                j += 1
            if self.__data[k] <= self.__data[j]:
                break
            self.__data[k], self.__data[j] = self.__data[j], self.__data[k]
            k = j
                
    def size(self):
        return self.__count
    
    def is_empty(self):
        return self.__count == 0
    
    def insert(self, item):
        assert self.__count + 1 <= self.__capacity
        self.__data[self.__count + 1] = item
        self.__count += 1
        self.__shift_up(self.__count)
        #print(self.__data)
        
    def extract_min(self):
        assert self.__count > 0
        ret = self.__data[1]
        self.__data[1], self.__data[self.__count] = self.__data[self.__count], self.__data[1]
        self.__count -= 1
        self.__shift_down(1)
        return ret
    
if __name__ == '__main__':
    min_heap = MinHeap(100)
#    print(max_heap.size())
#    
    np.random.seed(1023)
    for _ in range(15):
        min_heap.insert(np.random.randint(1, 100))
    print(min_heap.size())
#    
#    n = 15
#    arr = np.random.randint(0, 100, size = n)
#    max_heap = MaxHeap(arr, n)
    while not min_heap.is_empty():
        print(min_heap.extract_min())
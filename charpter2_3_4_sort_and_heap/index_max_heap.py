# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:42:16 2019

@author: Administrator
"""

import numpy as np

class IndexMaxHeap():
    
    def __init__(self, capacity):
        self.__data = [None] * (capacity + 1)
        self.__indexes = [None] * (capacity + 1)
        self.__reverse = [0] *(capacity + 1)
        self.__count = 0
        self.__capacity = capacity
#        
#    def __init__(self, arr, n):
#        self._data = [None] * (n + 1)
#        self._capacity = n
#        for i in range(n):
#            self._data[i + 1] = arr[i]
#        self._count = n
#        for i in range(int(self._count / 2), 0, -1):
#            self._shift_down(i)
#        print(self._data)
    
    def __shift_up(self, k):
        while(k > 1 and (self.__data[self.__indexes[int(k / 2)]] < self.__data[self.__indexes[int(k)]])):
            self.__indexes[int(k / 2)], self.__indexes[int(k)] = self.__indexes[int(k)], self.__indexes[int(k / 2)]
            self.__reverse[self.__indexes[int(k / 2)]] = int(k / 2)
            self.__reverse[self.__indexes[int(k)]] = int(k)
            k = int(k / 2) 
            
    def __shift_down(self, k):
        while 2 * k <= self.__count:
            j = 2 * k
            if j + 1 <= self.__count and self.__data[self.__indexes[j + 1]] > self.__data[self.__indexes[j]]:
                j += 1
            if self.__data[self.__indexes[k]] >= self.__data[self.__indexes[j]]:
                break
            self.__indexes[k], self.__indexes[j] = self.__indexes[j], self.__indexes[k]
            self.__reverse[self.__indexes[k]] = k
            self.__reverse[self.__indexes[j]] = j
            k = j
                
    def size(self):
        return self.__count
    
    def is_empty(self):
        return self.__count == 0
    
    def insert(self, i, item):
        assert self.__count + 1 <= self.__capacity
        assert i + 1 >= 1 and i + 1 <= self.__capacity
        i += 1
        self.__data[i] = item
        self.__indexes[self.__count + 1] = i
        self.__reverse[i] = self.__count + 1
        self.__count += 1
        self.__shift_up(self.__count)
        
    def extract_max(self):
        assert self.__count > 0
        ret = self.__data[self.__indexes[1]]
        self.__indexes[1], self.__indexes[self.__count] = self.__indexes[self.__count], self.__indexes[1]
        self.__reverse[self.__indexes[1]] = 1
        self.__reverse[self.__indexes[self.__count]] = 0
        self.__count -= 1
        self.__shift_down(1)
        return ret
    
    def extract_max_index(self):
        assert self.__count > 0
        ret = self.__indexes[1] - 1
        self.__indexes[1], self.__indexes[self.__count] = self.__indexes[self.__count], self.__indexes[1]
        self.__reverse[self.__indexes[1]] = 1
        self.__reverse[self.__indexes[self.__count]] = 0
        self.__count -= 1
        self.__shift_down(1)
        return ret
    
    def contain(self, i):
        assert i + 1 >= 1 and i + 1 <= self.__capacity
        return self.__reverse[i + 1] != 0
    
    def get_item(self, i):
        assert self.contain(i)
        return self.__data[i + 1]
    
    def change(self, i, new_item):
        assert self.contain(i)
        i += 1
        self.__data[i] = new_item
        
#        for j in range(1, self._count + 1):
#            if self._indexes[j] == i:
#                self._shift_up[j]
#                self._shift_down[j]
#                return
        j = self.__reverse[i]
        self.__shift_up(j)
        self.__shift_down(j)

if __name__ == '__main__':
    min_heap = IndexMaxHeap(15)
#    print(max_heap.size())
#    
    np.random.seed(1023)
    for i in range(15):
        min_heap.insert(i, np.random.randint(1, 100))
#    print(min_heap._IndexMinHeap__data)
#    print(min_heap._IndexMinHeap__indexes)
#    print(min_heap.size())
#    
#    n = 15
#    arr = np.random.randint(0, 100, size = n)
#    max_heap = MaxHeap(arr, n)
    while not min_heap.is_empty():
        print(min_heap.extract_max())
    
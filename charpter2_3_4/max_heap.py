# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:40:33 2019

@author: Administrator
"""
import numpy as np

class MaxHeap():
    
    def __init__(self, capacity):
        self.__data = [None] * (capacity + 1)
        self.__count = 0
        self.__capacity = capacity
#        
#    def __init__(self, arr, n):
#        self.__data = [None] * (n + 1)
#        self.__capacity = n
#        for i in range(n):
#            self.__data[i + 1] = arr[i]
#        self.__count = n
#        for i in range(int(self.__count / 2), 0, -1):
#            self.__shift_down(i)
#        print(self.__data)
    
    def __shift_up(self, k):
        while(k > 1 and (self.__data[int(k / 2)] < self.__data[int(k)])):
            self.__data[int(k / 2)], self.__data[int(k)] = self.__data[int(k)], self.__data[int(k / 2)]
            k = int(k / 2)
            
    def __shift_down(self, k):
        while 2 * k <= self.__count:
            j = 2 * k
            if j + 1 <= self.__count and self.__data[j + 1] > self.__data[j]:
                j += 1
            if self.__data[k] >= self.__data[j]:
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
        
    def extract_max(self):
        assert self.__count > 0
        ret = self.__data[1]
        self.__data[1], self.__data[self.__count] = self.__data[self.__count], self.__data[1]
        self.__count -= 1
        self.__shift_down(1)
        return ret
    
def heap_sort(arr):
    n = len(arr)
    for i in range(int((n - 1) / 2), -1, -1):
        __shift_down(arr, n, i)
        
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        __shift_down(arr, i, 0)
    
def __shift_down(arr, n, k):
    while 2 * k + 1 < n:
        j = 2 * k +1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        if arr[k] >= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j

if __name__ == '__main__':
    max_heap = MaxHeap(100)
#    print(max_heap.size())
#    
    np.random.seed(1023)
    for _ in range(15):
        max_heap.insert(np.random.randint(1, 100))
    print(max_heap.size())
#    
#    n = 15
#    arr = np.random.randint(0, 100, size = n)
#    max_heap = MaxHeap(arr, n)
    while not max_heap.is_empty():
        print(max_heap.extract_max())
    
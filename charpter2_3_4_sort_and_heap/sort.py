# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:39:35 2019

@author: Administrator
"""

import numpy as np
import time
import copy
import max_heap



def generate_random_array(n, range_l, range_r):
    array = np.random.randint(range_l, range_r + 1, n)
    return array

def generate_nearly_ordered_array(n, swap_time):
    array = []
    for i in range(n):
        array.append(i)
    for _ in range(swap_time):
        x_pos = np.random.randint(0, n)
        y_pos = np.random.randint(0, n)
        array[x_pos], array[y_pos] = array[y_pos], array[x_pos]
    return array

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def test_sort(sort_name, sort, array):
    start_time = time.time()
    sort(array)
    end_time = time.time()
    assert(is_sorted(array))
    print('%s : %ss' % (sort_name, end_time - start_time))
    
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        e = array[i]
        j = i
        while j >= 1 and e < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = e
    return array
        
def shell_sort(array):
    for h in [100, 10, 1]:
        for i in range(1, len(array)):
            e = array[i]
            j = i
            while j - h >= 0 and e < array[j - h]:
                array[j] = array[j - h]
                j -= h
            array[j] = e
            
def __merge_sort(array, l, r):
#    if l >= r:
#        return
    if r - l <= 15:
        array[l: r + 1] = insertion_sort(array[l: r + 1])
        return 
    
    mid = int((l + r) / 2)
    __merge_sort(array, l, mid)
    __merge_sort(array, mid + 1, r)
    if array[mid] > array[mid + 1]:
        __merge(array, l, mid, r)
    
def __merge(array, l, mid, r):
    aux = copy.copy(array[l: r + 1])
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if i > mid:
            array[k] = aux[j - l]
            j += 1
        elif j > r:
            array[k] = aux[i - l]
            i += 1
        elif aux[i - l] > aux[j - l]:
            array[k] = aux[j - l]
            j += 1
        else:
            array[k] = aux[i - l]
            i += 1
          
def merge_sort(array):
    __merge_sort(array, 0, len(array) - 1)
    
def merge_sort_bottom_up(array):
    size = 1
    while size <= len(array):
        i = 0
        while i + size < len(array):
            __merge(array, i, i + size - 1, min(i + size + size - 1, len(array) - 1))
            i = i + size + size
        size += size
        
def __partition(array, l, r):
    array[np.random.randint(l, r + 1)], array[l] = array[l], array[np.random.randint(l, r + 1)]
    v = array[l]
    #array[l, j] =< v, array[j + 1, i) > v
    j = l
    i = l + 1
    while i <= r:
        if array[i] < v:
            array[j + 1], array[i] = array[i], array[j + 1]
            j += 1
        i += 1
    array[l], array[j] = array[j], array[l]
    return j
    
def __quick_sort(array, l, r):
#    if l >= r:
#        return
    if r - l <= 15:
        array[l: r + 1] = insertion_sort(array[l: r + 1])
        return 
    #array[l, p - 1] < array[p], array[p + 1, r] > array[p]
    p = __partition(array, l, r)
    __quick_sort(array, l, p - 1)
    __quick_sort(array, p + 1, r)
    
def quick_sort(array):
    __quick_sort(array, 0, len(array) - 1)
    
def __partition2(array, l, r):
    array[np.random.randint(l, r + 1)], array[l] = array[l], array[np.random.randint(l, r + 1)]
    v = array[l]
    #array[l + 1, i) <= v, array(j, r] >= v
    i = l + 1
    j = r
    while True:
        while(array[i] < v and i <= r):
            i += 1
        while(array[j] > v and j >= l + 1):
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    array[l], array[j] = array[j], array[l]
    return j
    
def __quick_sort2(array, l, r):
#    if l >= r:
#        return
    if r - l <= 15:
        array[l: r + 1] = insertion_sort(array[l: r + 1])
        return 
    #array[l, p - 1] < array[p], array[p + 1, r] > array[p]
    p = __partition2(array, l, r)
    __quick_sort2(array, l, p - 1)
    __quick_sort2(array, p + 1, r)
    
def quick_sort2(array):
    __quick_sort2(array, 0, len(array) - 1)
    
def __quick_sort_3_ways(array, l, r):
    if r - l <= 15:
        array[l: r + 1] = insertion_sort(array[l: r + 1])
        return
    #partition
    array[np.random.randint(l, r + 1)], array[l] = array[l], array[np.random.randint(l, r + 1)]
    v = array[l]
    #array[l+1, lt] < v, array[gt, r] > v, array[lt + 1, i) = v
    lt = l
    gt = r + 1
    i = l + 1
    while i < gt:
        if array[i] < v:
            array[i], array[lt + 1] = array[lt + 1], array[i]
            lt += 1
            i += 1
        elif array[i] > v:
            array[i], array[gt - 1] = array[gt - 1], array[i]
            gt -= 1
        else:
            i += 1
            
    array[l], array[lt] = array[lt], array[l]
    
    __quick_sort_3_ways(array, l, lt - 1)
    __quick_sort_3_ways(array, gt, r)
        
def quick_sort_3_ways(array):
    __quick_sort_3_ways(array, 0, len(array) - 1)
 
if __name__ == '__main__':
    np.random.seed(1023)
    n = 10000
    array = generate_random_array(n, 0 ,10)
#    array = generate_nearly_ordered_array(n, 10)
    array2 = copy.copy(array)
    array3 = copy.copy(array)
    array4 = copy.copy(array)
    array5 = copy.copy(array)
#    test_sort('selection_sort', selection_sort, array)
#    test_sort('insertion_sort', insertion_sort, array2)
#    test_sort('shell_sort', shell_sort, array3)
    
    test_sort('quick_sort', quick_sort, array)
    test_sort('quick_sort2', quick_sort2, array2)
    test_sort('quick_sort_3_ways', quick_sort_3_ways, array4)
    test_sort('merge_sort', merge_sort, array3)
    test_sort('heap_sort', max_heap.heap_sort, array5)
    
#    test_sort('merge_sort_bottom_up', merge_sort_bottom_up, array2)
#    test_sort('insertion_sort', insertion_sort, array2)

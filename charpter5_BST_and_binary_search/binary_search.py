# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:49:20 2019

@author: Administrator
"""

def binary_search(arr, n, target):
    
    l, r = 0, n - 1
    
    while l <= r:
        
#        mid = int((l + r) / 2)
        mid = int(l + (r - l) / 2)
        
        if arr[mid] == target:
            return mid
        
        if target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:37:01 2019

@author: pranjal
"""

def binarySearch(arr,key,l,r,):
    if r-l == 0:
        return
    mid = (l+r)//2
    if key == arr[mid]:
        return(True)
    if key < arr[mid]:
        return(binarySearch(arr,key,l,mid))
    if key > arr[mid]:
        return(binarySearch(arr,key,mid,r))
        
    
n = int(input("Enter Number of elements in array :"))
arr = []
for _ in range(1,n+1):
    arr = arr+ [int(input('Enter element : '))]
key = int(input("Enput element to be search : "))
result = binarySearch(arr,key,0,n)
print()
if result==True:
    print("key is in the List")
else:
    print("key is not in the list")

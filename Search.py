#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:13:55 2019

@author: pranjal
"""

#Normal Search Program in Python

def search(List,key):
    i=0
    found=False
    if key in List:
        (found)=(True)
        print(' The Key '+str(key)+' is in the list.')
        return
    if found == False:
        print('Key is not in the List')


length = int(input('Enter the Number of Elements : '))
List = []
print(length)
for i in range(0,length):
    x = int(input('Enter the elements '))
    List.append(x)

print('Your list is : ' + str(List))  

key = int(input('Enter the Key to be found '))
search(List,key)
    
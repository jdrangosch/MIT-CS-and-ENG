#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:59:45 2024

@author: juls
"""

# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that prints hello world on separate lines, N times. 
# You can use either a while loop or a for loop.

N = 8
# ------- Option 1
#for i in range(N):
#    print('hello world')
#--------

# ------- Option 2
while N > 0:
    print('hello world')
    N = N - 1
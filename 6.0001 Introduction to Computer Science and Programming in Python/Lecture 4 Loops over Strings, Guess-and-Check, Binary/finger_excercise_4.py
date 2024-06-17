#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:06:58 2024

@author: juls
"""

# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube 
# or it prints error if N is not a perfect cube. 
# Hint: use a loop that increments a counter—you decide when the counter should stop.

N = abs(int(input("Enter a number: ")))

for guess in range(N+1):
    if guess**3 >= N:
        break

if guess**3 != N:
    print("error")
else:
    print(N,"is a perfect cube")
    
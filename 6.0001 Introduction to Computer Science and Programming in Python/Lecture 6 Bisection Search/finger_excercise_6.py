#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Fri May 31 22:40:56 2024

# @author: juls
# """

# Assume you are given an integer 0 \<= N \\<= 1000. Write a piece of Python code
# that uses bisection search to guess N. The code prints two lines: count: 
# with how many guesses it took to find N, and answer: with the value of N. 
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.


N = 599
count = 0
low = 0
high = 1000
guess = (low + high) / 2.0

# while (guess - N) // 1 != 0:
while abs(guess - N) > 0 :
    if guess - N < 0 :
        low = guess
    else :
        high = guess
    guess = (low + high)/2.0
    count += 1
print("Count: ", count)
print("Guess: ", guess)
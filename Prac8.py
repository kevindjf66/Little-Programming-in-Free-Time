# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:36:12 2017

@author: Kevin Deng
"""

#for the range(0,1000), print out all the Narcissistic numbers

for n in range(0, 1000):
    a = n % 10
    b = (n / 10) % 10
    c = (n / 100) % 10
    if a**3 + b**3 + c**3 == n:
        print n

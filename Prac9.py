# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:36:12 2017

@author: Kevin Deng
"""

#prime factorization for a number

n = int(raw_input('Please enter your number:'))
print '{} = '.format(n),
if n == 1:
    print '1 = 1'
else:
    while n != 1:
        for i in range(2, n+1):
            if n == 1:
                break
            if n % i == 0:
                print '{} * '.format(i),
                n = n / i
print '{}'.format(1),

#I just heard that format.(x) is better than %s, so I changed all %s to format.(x)

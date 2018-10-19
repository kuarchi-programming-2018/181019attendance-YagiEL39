# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:57:19 2018

@author: Takuto
"""
def fib(n):
    a,b=0,1
    if n==0:
        return a
    else:
        for i in range(n):
            a,b=b,a+b
        return b
print(fib(2018))
print(fib(5))
# -*- coding: utf-8 -*-

def fib(n):
    x=0
    y=1
    if n==0:
        return x
    else:
        for i in range(n):
            z=x+y
            x=y
            y=z
        return z
print(fib(2018)) 
#!/bin/python

import sys


def factorial(n):

    if n == 1:
        return n
    else:
        n = n * factorial(n-1)
        return n

    
i = int(raw_input().strip()) 

print str(factorial(i))

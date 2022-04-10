from math import sqrt
from decimal import *

def fib(n):
    getcontext.prec = 2000
    return Decimal(((1+sqrt(5))**n - (1-sqrt(5))**n)/(2**n * sqrt(5)))

for i in range(900):
    print(i, fib(i))
    if len(str(fib(i))) > 1000:
        print(i)
        break

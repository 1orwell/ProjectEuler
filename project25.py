from math import sqrt
from decimal import *

def fib(n):
    # use Decimal precision to be able to use enough digits
    getcontext().prec = 2000
    # Can't use recursion as reach recursion limit very quickly
    return ((Decimal(1)+Decimal(sqrt(5)))**Decimal(n) - (Decimal(1)-Decimal(sqrt(5)))**Decimal(n))/(Decimal(2)**Decimal(n) * Decimal(sqrt(5)))

for i in range(100000000000000):
    # round to get rid of decimals before finding length
    num = round(fib(i))
    #print(i, num, len(str(num)))
    if len(str(num)) == 1000:
        print(i)
        break

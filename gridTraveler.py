from threading import get_ident

#oh my gosh, it worked
def gridTraveler(m,n,memo):
    if m == 1 and n == 1:
        return 1
    if m==0 or n == 0:
        return 0
    elif (m,n) in memo:
        return memo[(m,n)]
    #number of paths will be the same, just rotated grid by 90 degrees
    elif (n,m) in memo:
        return memo[(n,m)]
    else:
        memo[(m,n)] = gridTraveler(m-1,n,memo) + gridTraveler(m,n-1,memo)
    return memo[m,n]

options = gridTraveler(20,20,{})
print(options)
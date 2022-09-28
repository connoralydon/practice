
from symbol import factor


def factorial(n):
    res = 1
    
    # we don't need recursion here
    # 5! = 5 * 4 * 3 * 2 * 1
    
    for i in range(2,n+1):
        res *= i
    
    return res




def permutation(n, r):
    # nPr = n! / (n-r)!
    
    res = factorial(n) / factorial(n-r)
    
    return res

def combination(n,r):
    # nCr = nPr / r! = n! / ((n-r)! * r!)
    
    res = permutation(n,r) / factorial(r)

    return res


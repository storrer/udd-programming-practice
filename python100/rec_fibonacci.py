"""
Input  1 2 3 4 5 6 7 8
fib(n) 1 1 2 3 5 8 13 21
n = 1, f(n) = 1
n = 2, f(n) = 1
n = 3, f(n) = f(3-1)+f(3-2) = 1 + 1
"""

def rec_fib(n):
    if n == 1 or n == 2:
        return 1
    #if n == 2:
    #    return 1
    return rec_fib(n-1) + rec_fib(n-2)
print(rec_fib(4))
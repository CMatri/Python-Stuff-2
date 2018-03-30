import math

def factorial(n):
    if n == 1: return n
    return factorial(n - 1) * n

def eulers(n):
    res = 1
    for i in range(1, n):
        res += 1 / factorial(i)
    return res

a = 3.141592653589793238462643383j
print(eulers(500))

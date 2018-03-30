n = 600851475143
factors = []
d = 2

while n > 1:
    while n % d == 0:
        factors.append(d)
        n /= d
    d += 1

print(factors)
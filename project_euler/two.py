s = 0

def fib(a, b, cnt):
    global s
    cnt -= 1
    if b < 4000000 and b % 2 == 0:
        s += b
    elif b >= 4000000 or not cnt:
        return a + b
    print(b)
    return fib(b, a + b, cnt)

print(fib(1, 2, 1000000))
print(s)
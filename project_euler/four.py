pal = lambda a: int(str(a)[::-1]) == a
largest = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        if pal(i * j) and largest < i * j: largest = i * j

print(largest)
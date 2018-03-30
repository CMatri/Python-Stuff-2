p = 20

while True:
    t = True
    for i in range(1, 21):
        if p % i != 0: 
            t = False
            break
    if t: break
    p += 20

print('Answer: ', p)
    
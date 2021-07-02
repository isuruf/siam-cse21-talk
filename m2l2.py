import matplotlib.pyplot as plt
import numpy as np
mis = []
n = 5
mis.extend((0, i) for i in range(n+1))
mis.extend((1, i) for i in range(n))
print(mis)

gs = set()
for i in range(2*n+1):
    for j in range(3):
        k = (j, i)
        gs.add(k)

gs = sorted(list(gs))
print(gs)

arr = np.zeros((len(gs), len(gs)))
for i, m1 in enumerate(mis):
    for j, m2 in enumerate(mis):
        k = (m1[0]+m2[0], m1[1]+m2[1])
        arr[gs.index(m1), gs.index(k)] = j+1
        #arr[len(mis)-1 - i, len(mis)-1 - j] = gs.index(k)

plt.imshow(arr)
plt.show()

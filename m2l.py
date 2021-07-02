import matplotlib.pyplot as plt
import numpy as np
mis = []
n = 4
m = 2
for j in range(m):
    mis.extend((j, i) for i in range(n+1-j))

gs = set()
for i in mis:
    for j in mis:
        k = (i[0]+j[0], i[1]+j[1])
        gs.add(k)

gs = sorted(list(gs))
print(gs, len(gs))
import random
values = list(range(len(gs)))
#random.shuffle(values)

arr = np.zeros((len(mis), len(mis)))
for i, m1 in enumerate(mis):
    for j, m2 in enumerate(mis):
        k = (m1[0]+m2[0], m1[1]+m2[1])
        #arr[gs.index(m1), gs.index(k)] = j+1
        #arr[i, len(mis)-1 - j] = gs.index(k) + 1
        arr[i, j] = gs.index(k) + 1
        arr[i, j] = values[gs.index(k)]

"""
s = (n+1)*(2*m-1)-1
arr2 = np.zeros((s, s)) - 1
for i in range(len(mis)):
    for j in range(len(mis)):
        m1 = mis[i]
        m2 = mis[j]
        r = m1[0]*(n+1)*2 + m1[1]
        c = m2[0]*(n+1)*2 + m2[1]
        print(m1, m2, i, j, r, c)
        arr2[r, c] = arr[i, j]


for k in range(2*s-1):
    val = -1
    for i in range(max(0, k-s+1), min(k, s)):
        j = k - i
        print(i, j, k, s)
        if arr2[i, j] != -1:
            val = arr2[i, j]
    for i in range(max(0, k-s+1), min(k, s)):
        j = k - i
        arr2[i, j] = val

print(arr)
masked_array = np.ma.masked_where(arr2 == -1, arr2)

import matplotlib.cm
import copy
cmap = copy.copy(matplotlib.cm.get_cmap())
cmap.set_bad(color='white')
"""

s2 = len(gs)//2
arr2 = np.zeros((s2+1, s2))
for i in range(s2+1):
    for j in range(s2):
        arr2[i, j] = i + j +1
        arr2[i, j] = values[i+j]

print(s2+s2)
print(mis)

def ticks(mis, name):
    res = ["a"]
    for mi in mis:
        d = "y" * mi[0] + "x" * mi[1]
        tick = f"${name}_{{{d}}}$"
        if mi == (0, 0):
            tick = f"${name}$"
        print(mi, tick)
        res.append(tick)
    return res

xticks = ticks(mis, "C")
yticks = ticks(mis, "T")
gticks = ticks(gs, "G")[1:]


plt.imshow(arr, cmap="hsv")
plt.plot([-0.5, 8.5], [4.5, 4.5], color="black")
plt.plot([4.5, 4.5], [-0.5, 8.5], color="black")
plt.title("Multipole to Local translation Matrix for Laplace 2D")
ax = plt.gca()
ax.set_xticklabels(xticks)
ax.set_yticklabels(yticks)
plt.xlabel("Source coeffcients")
plt.ylabel("Target coeffcients")
cbar = plt.colorbar()
cbar.set_ticks(list())
for i, g in enumerate(gs):
    cbar.ax.text(0.25, i-0.25, gticks[i])
#cbar.ax.set_yticks(np.linspace(0, 4.5, len(gs)))
#cbar.ax.set_yticklabels(gticks)
plt.tight_layout()
plt.savefig("figures/m2l_imshow.pdf")
plt.clf()


print(arr2)
xticks = ticks(mis, "C")[1:]
yticks = ticks(mis, "T")[1:]
plt.imshow(arr2, cmap="hsv")
plt.plot([-0.5, 11.5], [4.5, 4.5], color="black")
plt.plot([-0.5, 11.5], [8.5, 8.5], color="black")
plt.plot([4.5, 4.5], [-0.5, 12.5], color="black")
plt.plot([7.5, 7.5], [-0.5, 12.5], color="black")
plt.title("M2L translation Matrix with dummy rows and columns for Laplace 2D")
print(xticks)
for i in range(3):
    xticks.insert(5, "*")
for i in range(4):
    yticks.insert(5, "*")
ax = plt.gca()
ax.set_xticks(list(range(12)))
ax.set_yticks(list(range(13)))
ax.set_xticklabels(xticks)
ax.set_yticklabels(yticks)
plt.xlabel("Source coeffcients")
plt.ylabel("Target coeffcients")
cbar = plt.colorbar()
cbar.set_ticks(list())
for i, g in enumerate(gs):
    cbar.ax.text(0.25, i-0.25, gticks[i])
plt.tight_layout()
plt.savefig("figures/m2l_imshow_2.pdf")

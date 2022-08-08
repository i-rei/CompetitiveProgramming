import math
n = int(input())
a = list(map(int, input().split()))
c = []
ans = 0
for i in range(len(a)):
    x = a[i]
    if x is not None:
        if x == i + 1:
            c.append(i)
        elif a[x - 1] == i + 1:
            ans += 1
            a[x - 1] = None
print(ans + math.comb(len(c), 2))

from collections import defaultdict
n = int(input())
d = defaultdict(int)
a = [0] * n
for i in range(n):
    x = input()
    a[i] = x
    d[x] += 1
    c = d[x]
    if c != 1:
        a[i] = a[i] + "({})".format(c - 1)

for i in a:
    print(i)

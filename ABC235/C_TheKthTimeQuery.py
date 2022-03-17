from collections import defaultdict
n, q = map(int, input().split())
a = tuple(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    d[a[i]].append(i + 1)


for i in range(q):
    x, y = map(int, input().split())
    if len(d[x]) < y:
        print(-1)
    else:
        print(d[x][y - 1])

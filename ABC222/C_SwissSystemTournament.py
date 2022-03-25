from collections import defaultdict
n, m = map(int, input().split())
a = defaultdict(list)
v = dict()
r = [0] * (2 * n)
for i in range(2 * n):
    a[i] = list(input())
    r[i] = (i, 0)
    v[i] = 0

for i in range(m):
    for k in range(1, n + 1):
        x, y = r[2 * k - 2][0], r[2 * k - 1][0]
        if a[x][i] == "G" and a[y][i] == "C":
            v[x] += 1
        elif a[x][i] == "G" and a[y][i] == "P":
            v[y] += 1
        elif a[x][i] == "C" and a[y][i] == "G":
            v[y] += 1
        elif a[x][i] == "C" and a[y][i] == "P":
            v[x] += 1
        elif a[x][i] == "P" and a[y][i] == "G":
            v[x] += 1
        elif a[x][i] == "P" and a[y][i] == "C":
            v[y] += 1
    r = sorted(v.items(), key=lambda z: z[1], reverse=True)
for i in r:
    print(i[0] + 1)

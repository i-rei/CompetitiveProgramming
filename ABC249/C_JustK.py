import itertools
from collections import defaultdict
n, k = map(int, input().split())
s = [list(input()) for i in range(n)]
r = []
for i in range(1, len(s) + 1):
    for j in itertools.combinations(s, i):
        r.append(list(j))

ans = 0
for i in r:
    c = defaultdict(int)
    r = 0
    for j in i:
        for m in j:
            c[m] += 1
    for m in list(c.values()):
        if m == k:
            r += 1
    ans = max(ans, r)
print(ans)

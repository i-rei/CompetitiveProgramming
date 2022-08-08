from itertools import combinations
from collections import defaultdict
n, m = map(int, input().split())
b = defaultdict(list)
ans = 0
for i in range(m):
    u, v = map(int, input().split())
    b[u].append(v)

for key, value in list(b.items()):
    if len(value) >= 2:
        c = list(combinations(value, 2))
        for i in c:
            x, y = i[0], i[1]
            if y in b[x] or x in b[y]:
                ans += 1
print(ans)

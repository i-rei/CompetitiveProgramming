# 参考 https://kabukimining.hateblo.jp/entry/2019/12/23/152913
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = 1
for i in range(n):
    if a[i] == c:
        c += 1
    else:
        a[i] = 0
r = Counter(a)[0]
if r == n:
    print("-1")
else:
    print(r)

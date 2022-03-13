# 参考：https://qiita.com/sano192/items/6a9ba0ccb5b3c1538a84#c---collision-2
from collections import defaultdict
n = int(input())
x = [list(map(int, input().split())) for i in range(n)]
y = set()
for i in x:
    y.add(i[1])
s = input()

L, R = defaultdict(list), defaultdict(list)

for i in range(n):
    if s[i] == "L":
        L[x[i][1]].append(x[i][0])
    else:
        R[x[i][1]].append(x[i][0])

for i in y:
    if len(L[i]) > 0 and len(R[i]) > 0:
        if max(L[i]) > min(R[i]):
            print("Yes")
            exit()
print("No")

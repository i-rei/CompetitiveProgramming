import collections
n = int(input())
a = []
for i in range(n - 1):
    x, y = map(int, input().split())
    a.append(x)
    a.append(y)
c = collections.Counter(a)
if n - 1 in c.values():
    print("Yes")
else:
    print("No")

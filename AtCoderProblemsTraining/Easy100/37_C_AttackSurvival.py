import collections
n, k, q = map(int, input().split())
a = [0] * q
for _ in range(q):
    a[_] = int(input())
c = collections.Counter(a)
r = [k - q + c[i] if i in c.keys() else k - q for i in range(1, n + 1)]
for i in r:
    print("Yes") if i > 0 else print("No")

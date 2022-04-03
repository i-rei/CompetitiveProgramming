n, m = map(int, input().split())
L, R = [0] * m, [0] * m
for i in range(m):
    L[i], R[i] = map(int, input().split())
c = [x for x in range(max(L), min(R) + 1)]
a = [max(L), min(R)]
if a[0] <= a[1]:
    print(a[0] - a[1] + 1)
else:
    print(0)

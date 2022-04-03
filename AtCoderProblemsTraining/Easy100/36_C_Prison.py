n, m = map(int, input().split())
L, R = [0] * m, [0] * m
for i in range(m):
    L[i], R[i] = map(int, input().split())
c = [max(L), min(R)]
if c[0] <= c[1]:
    print(c[0] - c[1] + 1)
else:
    print(0)

n, k = map(int, input().split())
a = list(map(int, input().split()))
A = sorted(a)
if a == A:
    print('Yes')
    exit()
b = []
for i in range(k):
    b.append(sorted([a[j] for j in range(i, n, k)]))
c = [0] * n
for i, x in enumerate(b):
    for j, y in enumerate(x):
        c[i + j * k] = y
if c == A:
    print('Yes')
else:
    print('No')

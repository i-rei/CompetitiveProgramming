import math
n = int(input())
a, b = [], []
result = 0

for i in range(n):
    m, n = map(int, input().split())
    a.append(m)
    b.append(n)

for j in range(n):
    for k in range(j + 1, n):
        m = a[j] - a[k]
        n = b[j] - b[k]
        print(m, n)
        result = max(result, math.sqrt(m * m + n * n))

print(result)

import math
n = int(input())
a, b = [], []

for i in range(n):
    m, n = map(int, input().split())
    a.append(m)
    b.append(n)
result = 0
for j in range(n):
    for i in range(j+1, n):
        m = a[j] - a[i]
        n = b[j] - b[i]
        print(m, n)
        result = max(result, math.sqrt(m * m + n * n))

print(result)

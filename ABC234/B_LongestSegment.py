import math
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = tuple(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(n):
        x = a[i][0] - a[j][0]
        y = a[i][1] - a[j][1]
        result = (max(result, math.sqrt(x ** 2 + y ** 2)))

print(result)

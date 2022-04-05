n = int(input())
p = list(map(int, input().split()))
r = 1
m = n + 1
for i in range(1, n):
    m = min(m, p[i - 1])
    if p[i] <= m:
        r += 1
print(r)

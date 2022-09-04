n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
x = sum(a[:m])
b = n - m + 1
for i in range(b):
    if i == 0:
        s = sum([a[k] * (k + 1) for k in range(m)])
        ans = s
    else:
        s = s - x + a[i + m - 1] * m
        ans = max(ans, s)
        if i != b - 1:
            x = x - a[i - 1] + a[i + m - 1]
print(ans)

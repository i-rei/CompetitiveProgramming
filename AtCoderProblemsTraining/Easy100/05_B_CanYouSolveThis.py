n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    r = [a[i][k] * b[k] for k in range(m)]
    if sum(r) + c > 0:
        ans += 1
print(ans)

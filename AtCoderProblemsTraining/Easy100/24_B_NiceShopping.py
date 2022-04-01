a, b, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(m)]
ans = min(al) + min(bl)
for i in range(m):
    ans = min(ans, al[c[i][0] - 1] + bl[c[i][1] - 1] - c[i][2])
print(ans)

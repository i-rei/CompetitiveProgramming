n, m = map(int, input().split())
r = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    r[a - 1] += 1
    r[b - 1] += 1
for i in r:
    print(i)

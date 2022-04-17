n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])
r = 10 ** 9 + 1
for i in range(n - k + 1):
    r = min(r, h[i + k - 1] - h[i])
print(r)

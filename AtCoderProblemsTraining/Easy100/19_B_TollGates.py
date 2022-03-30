n, m, x = map(int, input().split())
a = list(map(int, input().split()))
c = [0, 0]
for i in range(1, n - x + 1):
    if x + i in a:
        c[0] += 1
for i in range(x):
    if i in a:
        c[1] += 1
print(min(c))

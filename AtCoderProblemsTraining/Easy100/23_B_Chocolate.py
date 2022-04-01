n = int(input())
d, x = map(int, input().split())
a = [0] * n
r = 0
for i in range(n):
    a[i] = int(input())
for i in a:
    for k in range(1, d + 1, i):
        r += 1
print(r + x)

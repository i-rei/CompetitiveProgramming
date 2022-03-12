n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
r = 0
for i in range(n):
    if a[i] == b[i]:
        r += 1
print(r)
a = set(a)
b = set(b)
c = b - a
print(n - len(c) - r)

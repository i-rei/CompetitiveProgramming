n, t = map(int, input().split())
a = list(map(int, input().split()))
r = 0
for i in range(n):
    for j in range(i, len(a)):
        if t == sum(a[i:j + 1]):
            r += 1
print(r)

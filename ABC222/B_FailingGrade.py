n, p = map(int, input().split())
a = tuple(map(int, input().split()))
r = 0
for i in a:
    if i < p:
        r += 1
print(r)

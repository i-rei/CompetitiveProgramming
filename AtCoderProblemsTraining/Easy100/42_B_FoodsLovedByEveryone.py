n, m = map(int, input().split())
a = [list(map(int, input().split()))[1:] for _ in range(n)]
r = 0
for i in range(1, m + 1):
    c = 0
    for j in a:
        if i in j:
            c += 1
    if c == n:
        r += 1
print(r)

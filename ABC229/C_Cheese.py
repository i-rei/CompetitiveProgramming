n, w = map(int, input().split())
cheese = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a in cheese:
        cheese[a] += b
    else:
        cheese[a] = b
c = sorted(cheese)
c.reverse()

rd = 0
i = 0
while w > 0 and i < n:
    a = c[i]
    if w - cheese[a] == 0:
        rd += a * cheese[a]
        w -= cheese[a]
        print(rd)
        exit()
    elif w - cheese[a] > 0:
        rd += a * cheese[a]
        w -= cheese[a]
    else:
        rd += a * w
        print(rd)
        exit()
    i += 1
print(rd)

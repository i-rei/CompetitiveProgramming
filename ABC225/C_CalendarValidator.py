n, m = map(int, input().split())
a = list(list(map(int, input().split())) for i in range(n))
m_max = 9 - m
maybe = []
for j in range(1, m_max):
    key = a[0][0]
    i = (key - j) / 7 + 1
    if i.is_integer():
        maybe.append((int(i), j))
r = []
for i, j in maybe:
    for x in range(i, i + n):
        rr = []
        for y in range(j, j + m):
            rr.append((x - 1) * 7 + y)
        r.append(rr)

if r == a:
    print("Yes")
else:
    print("No")

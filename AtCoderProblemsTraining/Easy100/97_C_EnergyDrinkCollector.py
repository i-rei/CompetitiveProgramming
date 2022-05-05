n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
a.sort()
r = 0
for i in a:
    p, q = i[0], i[1]
    if m >= q:
        m -= q
        r += p * q
    else:
        r += p * m
        print(r)
        exit()
print(r)

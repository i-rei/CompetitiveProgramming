import itertools
h, w = map(int, input().split()) a = [list(map(int, input().split())) for i in range(h)]
i_l, j_l = set(), set()
for i in range(1, h + 1):
    for j in range(i + 1, h + 1):
        t = (i, j)
        i_l.add(t)
for i in range(1, w + 1):
    for j in range(i + 1, w + 1):
        t = (i, j)
        j_l.add(t)
c = tuple(itertools.product(i_l, j_l))
for p in c:
    i1, i2, j1, j2 = p[0][0] - 1, p[0][1] - 1, p[1][0] - 1, p[1][1] - 1
    if not a[i1][j1] + a[i2][j2] <= a[i2][j1] + a[i1][j2]:
        print("No")
        exit()
print("Yes")

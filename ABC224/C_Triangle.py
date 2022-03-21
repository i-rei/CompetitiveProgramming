import itertools
n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]
cl = []
for i in itertools.combinations(p, 3):
    cl.append(i)
r = 0

for i in cl:
    a, b, c = i[0], i[1], i[2]
    s = abs((a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])) * 0.5
    if not s == 0:
        r += 1

print(r)

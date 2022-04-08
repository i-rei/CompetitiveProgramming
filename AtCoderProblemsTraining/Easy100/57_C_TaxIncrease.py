from math import floor
a, b = map(int, input().split())
ra, rb = [0] * 10, [0] * 10
for i in range(10):
    ra[i] = floor(float(f"{(a + i / 10) / 0.08:.1f}"))
    rb[i] = floor(float(f"{(b + i / 10) / 0.1:.1f}"))
r = []
for i in ra:
    if i in rb and floor(i * 0.08) == a and floor(i * 0.1) == b:
        r.append(i)
if not r:
    print(-1)
else:
    print(r[0])

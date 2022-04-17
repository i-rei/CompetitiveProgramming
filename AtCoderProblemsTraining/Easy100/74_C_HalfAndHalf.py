a, b, c, x, y = map(int, input().split())
ab = min(a + b, c * 2)
m = min(x, y)
r = ab * m
if x - m > y - m:
    r += a * (x - m)
else:
    r += b * (y - m)
print(min(r, ab * max(x, y)))

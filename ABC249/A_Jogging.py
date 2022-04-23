import math
a, b, c, d, e, f, x = map(int, input().split())
r1 = a * b * math.floor(x / (a + c)) + min(x % (a + c), a) * b
r2 = d * e * math.floor(x / (d + f)) + min(x % (d + f), d) * e
if r1 > r2:
    print("Takahashi")
elif r1 < r2:
    print("Aoki")
else:
    print("Draw")

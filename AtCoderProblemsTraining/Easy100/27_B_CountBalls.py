from math import floor
n, a, b = map(int, input().split())
r = a * floor(n / (a + b))
if n % (a + b) < a:
    print(r + n % (a + b))
else:
    print(r + a)

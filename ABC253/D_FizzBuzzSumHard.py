import math
n, a, b = map(int, input().split())
sn = n * (n + 1) // 2
sa = n // a * (2 * a + (n // a - 1) * a) // 2
sb = n // b * (2 * b + (n // b - 1) * b) // 2
g = a * b // math.gcd(a, b)
sab = n // g * (2 * g + (n // g - 1) * g) // 2
print(sn - sa - sb + sab)

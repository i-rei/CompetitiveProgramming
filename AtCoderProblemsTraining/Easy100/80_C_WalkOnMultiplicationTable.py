from math import sqrt
n = int(input())
a = [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
r = 10 ** 13
for i in a:
    r = min(r, i - 1 + n // i - 1)
print(r)

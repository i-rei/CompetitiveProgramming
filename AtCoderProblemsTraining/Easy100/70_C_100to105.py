from math import floor
x = int(input())
mod = x % 100
n100 = floor(x / 100)
a = 0
for i in range(5, 0, -1):
    a += floor(mod / i)
    mod %= i
if a > n100:
    print(0)
else:
    print(1)

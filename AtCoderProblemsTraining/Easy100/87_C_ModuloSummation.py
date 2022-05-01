import math
import functools


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return functools.reduce(my_lcm_base, numbers, 1)


n = int(input())
a = list(map(int, input().split()))
x = my_lcm(*a) - 1
ans = 0
for i in a:
    ans += x % i
print(ans)

def func(t):
    return t * t + 2 * t + 3


n = int(input())
print(func(func(func(n) + n) + func(func(n))))

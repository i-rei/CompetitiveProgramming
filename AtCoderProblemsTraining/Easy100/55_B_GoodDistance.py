from math import sqrt
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
r = 0
for i, y in enumerate(x):
    for j in range(i + 1, len(x)):
        di = [(y[_] - x[j][_]) ** 2 for _ in range(d)]
        if sqrt(sum(di)).is_integer():
            r += 1
print(r)

from math import sqrt
a, b = map(int, input().split())
if a == 0:
    rx = 0
    if b > 0:
        ry = 1
    else:
        ry = -1
    print(rx, ry)
    exit()
c = b / a
rx = sqrt(1 / (1 + c ** 2))
ry = c * rx
print(rx, ry)

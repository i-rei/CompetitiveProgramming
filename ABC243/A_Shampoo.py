v, a, b, c = map(int, input().split())
i = 0
while v >= 0:
    i += 1
    v = v - a
    if v < 0:
        break
    i += 1
    v = v - b
    if v < 0:
        break
    i += 1
    v = v - c
    if v < 0:
        break
if i % 3 == 1:
    print("F")
elif i % 3 == 2:
    print("M")
else:
    print("T")

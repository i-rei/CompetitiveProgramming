n = int(input())
r = [1, 0]
for i in range(1, n + 1):
    c = 0
    a = i
    while True:
        if a % 2 == 0:
            c += 1
            a = a / 2
        else:
            break
    if c > r[1]:
        r = [i, c]
print(r[0])

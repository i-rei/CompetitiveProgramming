a = list(map(int, input().split()))
isOdd = [a[0] % 2 == 1, a[1] % 2 == 1, a[2] % 2 == 1]
s = 2
if isOdd.count(True) == 2:
    s = 0
elif isOdd.count(True) == 1:
    s = 1
r = 0
if not s == 2:
    r += 1
    if s == 0:
        for i in range(3):
            if isOdd[i]:
                a[i] += 1
    else:
        for i in range(3):
            if not isOdd[i]:
                a[i] += 1
m = max(a)
print(r + (m * 3 - sum(a)) // 2)

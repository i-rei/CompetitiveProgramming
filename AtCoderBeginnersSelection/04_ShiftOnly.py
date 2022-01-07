n = int(input())
a = list(map(int, input().split()))
isOK = False

s = 0

while not isOK:
    for i in range(n):
        if not a[i] % 2 == 0:
            isOK = True
            s -= 1
            break
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = round(a[i] / 2)

    s += 1

print(s)

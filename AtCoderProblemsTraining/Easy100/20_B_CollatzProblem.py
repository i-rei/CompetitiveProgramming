s = int(input())
a = [s]
i = 2
while True:
    if a[i - 2] % 2 == 0:
        c = a[i - 2] // 2
    else:
        c = 3 * a[i - 2] + 1
    if c in a:
        print(i)
        exit()
    else:
        a.append(c)
        i += 1

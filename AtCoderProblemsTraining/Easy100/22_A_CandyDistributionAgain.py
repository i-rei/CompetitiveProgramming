n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
for i in range(n):
    if x - a[i] >= 0:
        if i == n - 1 and x == a[i]:
            print(i + 1)
            exit()
        elif i == n - 1:
            print(i)
            exit()
        else:
            x -= a[i]
    else:
        print(i)
        exit()

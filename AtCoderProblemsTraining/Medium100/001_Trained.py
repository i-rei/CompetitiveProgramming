n = int(input())
a = [int(input()) for i in range(n)]
s = sum(a)
p = a[0]
i = 0
ans = 1
while True:
    if p == 2:
        print(ans)
        exit()
    elif p == 0:
        print(-1)
        exit()
    else:
        a[i] = 0
        i = p - 1
        p = a[i]
        ans += 1

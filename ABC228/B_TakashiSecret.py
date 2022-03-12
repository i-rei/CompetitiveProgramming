n, x = map(int, input().split())
a = list(map(int, input().split()))
s = [False] * len(a)
s[x - 1] = True
for i in range(len(a) - 1):
    x = a[x - 1]
    if s[x - 1] is False:
        s[x - 1] = True
    else:
        print(i + 1)
        exit()
print(n)

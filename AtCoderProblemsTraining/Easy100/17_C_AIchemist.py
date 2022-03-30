n = int(input())
a = sorted(list(map(int, input().split())))
i = 0
while len(a) > 1:
    a.append((a[0] + a[1]) / 2)
    del a[0]
    del a[0]
    a.sort()
print(a[0])

n = int(input())
a = list(map(int, input().split()))
x = list(filter(lambda z: z % 2 == 0, a))
y = list(filter(lambda z: z % 2 == 1, a))
x.sort()
y.sort()
if len(y) < 2 and len(x) < 2:
    print(-1)
    exit()
elif len(y) < 2:
    print(sum(x[-2:]))
    exit()
elif len(x) < 2:
    print(sum(y[-2:]))
    exit()
print(max(sum(y[-2:]), sum(x[-2:])))

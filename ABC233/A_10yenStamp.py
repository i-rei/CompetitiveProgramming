a, b = map(int, input().split())
i = 0
if a >= b:
    print(0)
    exit()
while a < b:
    i += 1
    a += 10
    if a >= b:
        print(i)
        exit()

a, b, k = map(int, input().split())
if a >= b:
    print(0)
    exit()
i = 1
while True:
    a = a * k
    if a >= b:
        print(i)
        exit()
    else:
        i += 1

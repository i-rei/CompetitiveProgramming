n = int(input())
i = 0
while True:
    if 2 ** i == n:
        print(i)
        exit()
    elif 2 ** i > n:
        print(i - 1)
        exit()
    else:
        i += 1

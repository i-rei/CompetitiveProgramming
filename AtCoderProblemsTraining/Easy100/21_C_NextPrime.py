x = int(input())
while True:
    i = 2
    c = False
    while i * i <= x:
        if x % i == 0:
            c = True
            break
        i += 1
    if c:
        x += 1
    else:
        print(x)
        exit()

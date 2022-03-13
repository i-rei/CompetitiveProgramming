n = int(input())
a = tuple(tuple(map(int, input().split())) for i in range(n))
now = [0, 0, 0]
for i in a:
    t = i[0] - now[0]
    r = abs(now[1] - i[1]) + abs(now[2] - i[2])
    if now[1] == i[1] and now[2] == i[2] and t % 2 == 1:
        print("No")
        exit()
    elif r > t:
        print("No")
        exit()
    elif (t - r) % 2 == 1:
        print("No")
        exit()
    else:
        now = i
print("Yes")

n = int(input())
c = set(i for i in range(1, 2 * n + 2))
while len(c) > 0:
    m = c.pop()
    print(m)
    t = int(input())
    if t == 0:
        exit()
    c.remove(t)
exit()

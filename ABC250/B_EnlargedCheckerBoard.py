n, a, b = map(int, input().split())
t1, t2 = [0] * n, [0] * n
for i in range(n):
    if i % 2 == 0:
        t1[i] = "." * b
        t2[i] = "#" * b
    else:
        t2[i] = "." * b
        t1[i] = "#" * b
for i in range(n):
    if i % 2 == 0:
        for k in range(a):
            print("".join(t1))
    else:
        for k in range(a):
            print("".join(t2))

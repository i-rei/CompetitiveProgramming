s = input()
for i in range(len(s) - 1, -1, -1):
    x = s[:i]
    if len(x) % 2 == 0:
        m = len(x) // 2
        a, b = x[:m], x[m:]
        if a == b:
            print(len(x))
            exit()

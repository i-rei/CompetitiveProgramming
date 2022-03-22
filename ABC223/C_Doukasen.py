n = int(input())
a, b, sl = [0] * n, [0] * n, [0] * n
s = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
    sl[i] = a[i] / b[i]
    s += sl[i]
s = s / 2

r = 0
for i in range(n):
    if sl[i] < s:
        r += a[i]
        s -= sl[i]
    elif sl[i] == s:
        r += a[i]
        print(r)
        exit()
    else:
        r += b[i] * s
        print(r)
        exit()

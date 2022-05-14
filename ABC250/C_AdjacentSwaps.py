n, q = map(int, input().split())
a = [str(i + 1) for i in range(n)]
x = sorted([int(input()) for i in range(q)])
for i in range(q):
    if x[i] == 0:
        continue
    if i != q - 1:
        if x[i + 1] - x[i] == 1:
            x[i], x[i + 1] = 0, 0
x = sorted(set(x), key=x.index)
for i in x:
    if i != 0:
        w = a.index(str(i))
        if w == n - 1:
            a[w], a[w - 1] = a[w - 1], a[w]
        else:
            a[w], a[w + 1] = a[w + 1], a[w]
print(" ".join(a))

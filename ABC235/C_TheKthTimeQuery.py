n, q = map(int, input().split())
a = tuple(map(int, input().split()))
b = [0] * q
for i in range(q):
    t = tuple(map(int, input().split()))
    if t[0] in a and a.count(t[0]) >= t[1]:
        b[i] = t
for i in b:
    if i == 0:
        print("-1")
    else:
        c = [(k, a[k]) for k in range(n) if a[k] == i[0]]
        print(c[i[1] - 1][0] + 1)

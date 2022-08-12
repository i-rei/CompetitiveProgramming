x = list(input())
n = int(input())
names = [input() for i in range(n)]
d = dict()
for i in names:
    encodeN = []
    for a in list(i):
        encodeN.append(x.index(a) + 1)
    encodeN = tuple(encodeN)
    d[encodeN] = i

ans = sorted(d.items())
for i in ans:
    print(i[1])

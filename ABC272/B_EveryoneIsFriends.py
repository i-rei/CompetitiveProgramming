import itertools
n, m = map(int, input().split())
a = [0] * m
for i in range(m):
    x = list(map(int, input().split()))
    a[i] = x[1:]
p = list(itertools.combinations(range(1, n + 1), 2))
for i in p:
    c = False
    for k in a:
        if i[0] in k and i[1] in k:
            c = True
    if not c:
        print('No')
        exit()
print('Yes')

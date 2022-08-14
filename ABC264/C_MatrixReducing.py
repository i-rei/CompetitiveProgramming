from itertools import product
ah, aw = map(int, input().split())
a = [list(map(int, input().split())) for i in range(ah)]
bh, bw = map(int, input().split())
b = [list(map(int, input().split())) for i in range(bh)]

for h in product((0, 1), repeat=ah):
    for w in product((0, 1), repeat=aw):
        c = []
        for i, v in enumerate(h):
            if v == 1:
                c.append(a[i])
        for i, v in enumerate(c):
            x = []
            for k in range(aw):
                if w[k] == 1:
                    x.append(v[k])
            c[i] = x
        if b == c:
            print('Yes')
            exit()
print('No')
exit()

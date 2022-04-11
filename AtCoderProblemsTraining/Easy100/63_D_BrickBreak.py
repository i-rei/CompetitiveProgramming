n = int(input())
a = list(map(int, input().split()))
r = []
ri = [0]
if len(set(a)) == 1:
    print(-1)
    exit()
for i in range(max(a) + 1):
    if i in a:
        r.append(i)
        w = [x for x, y in enumerate(a) if y == i]
        print(i, w)
        for x in w:
            if x > max(ri):
                ri.append(x)
                w = []
        print(len(w), r, ri)
        if len(w) != 0:
            print(n - len(r))
            exit()
print(r)
if len(r) == 0:
    print(-1)
else:
    print(n - len(r))

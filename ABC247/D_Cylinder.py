from collections import deque
q = int(input())
r = deque([])
for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        r.append([a[1], a[2]])
    else:
        c = a[1]
        ok = False
        ans = 0
        while not ok:
            if c < r[0][1]:
                r[0][1] -= c
                ans += r[0][0] * c
                print(ans)
                ok = True
            elif c == r[0][1]:
                ans += r[0][0] * c
                print(ans)
                r.popleft()
                ok = True
            else:
                ans += r[0][0] * r[0][1]
                c -= r[0][1]
                r.popleft()

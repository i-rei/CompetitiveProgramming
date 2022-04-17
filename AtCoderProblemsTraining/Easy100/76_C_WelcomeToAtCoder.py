from collections import defaultdict
n, m = map(int, input().split())
r = [0, 0]
pr = defaultdict(list)
wa = 0
for i in range(m):
    p, s = input().split()
    pr[p].append(s)
for i in pr:
    if "AC" in pr[i]:
        r[0] += 1
        for k in pr[i]:
            if k == "WA":
                r[1] += 1
            else:
                break
print(str(r[0]) + " " + str(r[1]))

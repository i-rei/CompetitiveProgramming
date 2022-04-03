n = int(input())
s = list(input())
r = [0] * n
c = 0
for i, v in enumerate(s):
    if v == "I":
        c += 1
    else:
        c -= 1
    r[i] = c
r.append(0)
print(max(r))

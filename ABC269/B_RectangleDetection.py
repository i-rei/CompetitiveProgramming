s = [list(input()) for i in range(10)]
ab = []
cd = []
for i, v in enumerate(s):
    if set(v) != set('.'):
        ab.append(i + 1)
    if len(ab) == 1:
        for k, v2 in enumerate(v):
            if v2 == '#':
                cd.append(k + 1)
print(ab[0], ab[-1])
print(cd[0], cd[-1])

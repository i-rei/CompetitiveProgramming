s = list(input())
a = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        a.append(s[i:j])
r = a[:]
for i in a:
    for x in range(len(i)):
        if i[x] not in ["A", "C", "G", "T"]:
            r.remove(i)
            break
if not r:
    print(0)
else:
    print(max([len(r[i]) for i in range(len(r))]))

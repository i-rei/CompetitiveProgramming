a, b = [0] * 3, [0] * 3
for i in range(3):
    a[i], b[i] = map(str, input().split())
r = [0] * 2
c = set(a)
n = c.pop()
if a.count(n) == 1:
    r[0] = n
else:
    r[0] = c.pop()
c = set(b)
n = c.pop()
if b.count(n) == 1:
    r[1] = n
else:
    r[1] = c.pop()
print(" ".join(r))

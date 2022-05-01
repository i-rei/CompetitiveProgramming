n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]
ss = set(s)
r = 0
while ss:
    w = ss.pop()
    p, m = s.count(w), t.count(w)
    r = max(r, p - m)
print(r)

o = list(input())
e = list(input())
o.reverse()
e.reverse()
n = len(o) + len(e)
r = []
i = 0
while i < n:
    if i % 2 == 0:
        r.append(o.pop())
    else:
        r.append(e.pop())
    i += 1
print("".join(r))

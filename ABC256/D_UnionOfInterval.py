n = int(input())
ls = {0}
rs = {0}
for i in range(n):
    a, b = map(int, input().split())
    if a > max(rs):
        ls.add(a)
    rs.add(b)
print(ls)
print(rs)
ls = (list(ls))
rs = (list(rs))
ls.sort()
rs.sort()
for i in range(1, min(len(ls), len(rs))):
    print("{} {}".format(ls[i], rs[i]))

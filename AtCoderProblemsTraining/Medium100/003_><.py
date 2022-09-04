s = input()
ls = len(s)
ans = [0] * (ls + 1)
a = 1
for i in range(ls):
    if s[i] == '<':
        ans[i + 1] = a
        a += 1
    else:
        a = 1
a = 1
for i in range(ls - 1, -1, - 1):
    if s[i] == '>':
        ans[i] = max(ans[i], a)
        a += 1
    else:
        a = 1
print(sum(ans))

s = list(input())
ans = 0
c = 0
for i in s:
    if i == 'B':
        c += 1
    else:
        ans += c
print(ans)

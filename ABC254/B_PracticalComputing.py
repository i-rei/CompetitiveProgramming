n = int(input())
ans = []
for i in range(n):
    a = []
    for k in range(i + 1):
        if k == 0 or k == i:
            a.append(str(1))
        else:
            a.append(str(int(ans[i - 1][k - 1]) + int(ans[i - 1][k])))
    ans.append(a)

for i in ans:
    print(" ".join(i))

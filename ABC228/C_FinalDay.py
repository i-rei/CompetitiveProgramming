n, k = map(int, input().split())
s = list(sum(tuple(map(int, input().split()))) for i in range(n))
ss = sorted(s, reverse=True)
line = ss[k - 1]
for i in s:
    if i + 300 >= line:
        print("Yes")
    else:
        print("No")

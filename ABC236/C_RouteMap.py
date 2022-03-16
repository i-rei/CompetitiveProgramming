n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())
u = set(s) - set(t)
for i in range(n):
    if s[i] in u:
        print("No")
    else:
        print("Yes")

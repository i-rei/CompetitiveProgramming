n = int(input())
s, t = [0] * n, [0] * n
for i in range(n):
    s[i], t[i] = input().split()
for i in range(n):
    OK = False
    for a in [s[i], t[i]]:
        ok = True
        for j in range(n):
            if i != j:
                if a == s[j] or a == t[j]:
                    ok = False
        if ok:
            OK = True
    if not OK:
        print("No")
        exit()
print("Yes")

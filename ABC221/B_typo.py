s = input()
t = input()
if s == t:
    print("Yes")
    exit()
for i in range(len(s) - 1):
    a = list(s)
    a[i], a[i + 1] = s[i + 1], s[i]
    if "".join(a) == t:
        print("Yes")
        exit()
print("No")

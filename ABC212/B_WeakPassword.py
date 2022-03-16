p = list(input())
a = set(p)
c = 0
if len(a) == 1:
    print("Weak")
    exit()
for i in range(0, 3):
    if p[i] == "9" and p[i + 1] == "0":
        c += 1
    elif int(p[i + 1]) - int(p[i]) == 1:
        c += 1
if c == 3:
    print("Weak")
else:
    print("Strong")

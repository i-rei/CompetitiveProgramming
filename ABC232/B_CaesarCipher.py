import string

n = input()
t = input()
a = list(string.ascii_lowercase)
if a.index(t[0]) - a.index(n[0]) < 0:
    k = a.index(t[0]) - a.index(n[0]) + 26
else:
    k = abs(a.index(t[0]) - a.index(n[0]))


for i in range(len(n)):
    if a.index(t[i]) - a.index(n[i]) < 0:
        tmp = a.index(t[i]) - a.index(n[i]) + 26
    else:
        tmp = abs(a.index(t[i]) - a.index(n[i]))
    if not k == tmp:
        print("No")
        exit()
print("Yes")

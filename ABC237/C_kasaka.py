s = input()
c = [0] * 2
if s == s[::-1]:
    print("Yes")
    exit()


f = False
i = 0
if s[0] == "a":
    while not f:
        if s[i] == "a":
            i += 1
        else:
            c[0] = i
            f = True

f = False
i = -1
if s[-1] == "a":
    while not f:
        if s[i] == "a":
            i -= 1
        else:
            c[1] = i
            f = True
if c[0] == c[1]:
    ss = s
elif c[0] >= abs(c[1] + 1):
    print("No")
    exit()
elif c[0] < abs(c[1] + 1):
    tmp = c[1] + c[0] + 1
    ss = s[0: tmp]
else:
    ss = s[c[0]:len(s)]
    ss = ss[0: c[1] + 1]
if ss == ss[::-1]:
    print("Yes")
else:
    print("No")

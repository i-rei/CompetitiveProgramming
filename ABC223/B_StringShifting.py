s = input()
a = []
for i in range(len(s)):
    s = s[-1] + s[0:len(s) - 1]
    a.append(s)
a.sort()
print(a[0])
print(a[len(a) - 1])

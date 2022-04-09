s = list(input())
t = list(input())
for i in range(len(s)):
    a = s[-1]
    del s[-1]
    s.insert(0, a)
    if s == t:
        print("Yes")
        exit()
print("No")

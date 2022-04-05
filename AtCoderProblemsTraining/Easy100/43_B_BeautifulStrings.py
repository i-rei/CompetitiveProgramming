w = list(input())
c = set()
for i in w:
    if i not in c:
        c.add(i)
        if not w.count(i) % 2 == 0:
            print("No")
            exit()
print("Yes")

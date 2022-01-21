a = []
c = 0
for i in range(2):
    a.append(input())
if a[0] == '##':
    c += 1
if a[0][1] == a[1][1] and a[0][1] == "#":
    c += 1
if a[1] == "##":
    c += 1
if a[0][0] == a[1][0] and a[0][0] == "#":
    c += 1

if c >= 1:
    print("Yes")
else:
    print("No")

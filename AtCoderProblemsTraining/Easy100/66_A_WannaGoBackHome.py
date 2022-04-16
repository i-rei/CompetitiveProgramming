s = list(input())
r = [0, 0, 0, 0]
if "N" in s:
    r[0] = 1
if "W" in s:
    r[1] = 1
if "S" in s:
    r[2] = 1
if "E" in s:
    r[3] = 1
if sum(r) == 4:
    print("Yes")
elif sum(r) == 3:
    print("No")
elif r[0] == r[2] == 1 or r[1] == r[3] == 1:
    print("Yes")
else:
    print("No")

import math
n = input()
a = ""
for i in range(math.ceil((len(n) / 3) + 1)):
    a = a + "oxx"
if n in a:
    print("Yes")
else:
    print("No")

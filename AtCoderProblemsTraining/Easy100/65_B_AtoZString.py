s = list(input())
a = 0
z = 0
for i, x in enumerate(s):
    if x == "A":
        a = i
        break
s.reverse()
for i, x in enumerate(s):
    if x == "Z":
        z = len(s) - i
        break
print(z - a)

n = int(input())
f = list("HDCS")
s = list("A23456789TJQK")
a = set()
for i in range(n):
    t = input()
    if t[0] not in f:
        print("No")
        exit()
    if t[1] not in s:
        print("No")
        exit()
    a.add(t)
    if len(a) != i + 1:
        print("No")
        exit()
print("Yes")

a = [input() for i in range(3)]
t = list(input())
r = ""
for i in t:
    r = r + a[int(i) - 1]
print(r)

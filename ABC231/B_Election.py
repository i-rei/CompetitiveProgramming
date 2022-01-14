n = int(input())
a = []
for i in range(n):
    a.append(input())

b = list(set(a))
c = [0, '']
for i in range(len(b)):
    if c[0] < a.count(b[i]):
        c[0] = a.count(b[i])
        c[1] = b[i]
print(c[1])

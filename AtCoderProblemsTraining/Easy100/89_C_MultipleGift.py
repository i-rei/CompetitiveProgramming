x, y = map(int, input().split())
a = []
k = x
while k <= y:
    a.append(k)
    k *= 2
print(len(a))

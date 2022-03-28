n = int(input())
nl = list(map(int, input().split()))
a = 0
b = 0

for i in range(n):
    if i % 2 == 0:
        a += max(nl)
        del nl[nl.index(max(nl))]
    else:
        b += max(nl)
        del nl[nl.index(max(nl))]

print(a - b)

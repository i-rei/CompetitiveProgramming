a, b = map(int, input().split())
c = 1
i = 0
while c < b:
    c += a - 1
    i += 1
print(i)

n = int(input())
a = list(map(int, input().split()))
r = 0
for i in range(len(a)):
    if a[i] != 0:
        if a[a[i] - 1] - 1 == i:
            a[a[i] - 1] = 0
            a[i] = 0
            r += 1
print(r)

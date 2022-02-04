n = int(input())
a = list(map(int, input().split()))
r = a[0]
for i in range(n):
    if not r == a[n - 1]:
        if r < a[i + 1]:
            r = a[i + 1]
        else:
            print(r)
            exit()
print(r)

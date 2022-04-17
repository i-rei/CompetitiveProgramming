n = int(input())
a = sorted(list(map(int, input().split())))[n:]
r = 0
for i in range(0, len(a), 2):
    r += a[i]
print(r)

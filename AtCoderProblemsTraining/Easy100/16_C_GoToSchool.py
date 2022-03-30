n = int(input())
a = list(map(int, input().split()))
r = dict()
for i in range(1, n + 1):
    r[i] = a[i - 1]
ans = [str(i[0]) for i in sorted(r.items(), key=lambda x: x[1])]
print(" ".join(ans))

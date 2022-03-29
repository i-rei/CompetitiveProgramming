k, n = map(int, input().split())
a = list(map(int, input().split()))
b = [a[i + 1] - a[i] for i in range(n - 1)]
b.append(k - a[-1])

if a[0] == 0:
    print(k - max(b))
else:
    r = a[-1] - a[0]
    print(min(r, k - max(b)))

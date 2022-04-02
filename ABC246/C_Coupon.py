from math import floor
n, k, x = map(int, input().split())
a = list(map(int, input().split()))
u = 0
for i in range(n):
    if u + floor(a[i] / x) > k:
        a[i] -= x * (k - u)
        print(sum(a))
        exit()
    else:
        u += floor(a[i] / x)
        a[i] = a[i] % x
a.sort(reverse=True)
print(sum(a[k - u:]))

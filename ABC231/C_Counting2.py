n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))
mi = a[0]
ma = a[-1]
for i in range(q):
    x = int(input())
    r = 0
    if x < mi:
        print(n)
    elif ma < x:
        print(0)
    else:
        r1, r2 = 0, n - 1
        while r1 <= r2:
            mid = (r1 + r2) // 2
            if x < a[mid]:
                r2 = mid - 1
            if x > a[mid]:
                r1 = mid + 1
            if x == a[mid]:
                print(n - mid)
                break
            elif a[mid] < x <= a[mid + 1]:
                print(n - 1 - mid)
                break

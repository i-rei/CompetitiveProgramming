q, h, s, d = map(int, input().split())
n = int(input())
h1 = min(q * 4, h * 2, s)
h2 = min(h1 * 2, d)
if h1 * 2 <= d:
    print(h1 * n)
else:
    if n % 2 == 0:
        print(d * n // 2)
    else:
        print(d * (n - 1) // 2 + h1)

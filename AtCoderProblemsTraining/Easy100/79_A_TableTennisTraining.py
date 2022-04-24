n, a, b = map(int, input().split())
if a % 2 == b % 2 == 0 or a % 2 == b % 2 == 1:
    print(b - (a + b) // 2)
else:
    if a - 1 > n - b:
        print(n - b + 1 + (b - a - 1) // 2)
    else:
        print(a - 1 + 1 + (b - a - 1) // 2)

n, k, a = map(int, input().split())
x = (a + k - 1) % n
if x == 0:
    print(n)
else:
    print(x)

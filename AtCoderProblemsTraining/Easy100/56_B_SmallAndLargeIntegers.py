a, b, k = map(int, input().split())
if b - a < 2 * k:
    for i in range(a, b + 1):
        print(i)
    exit()
for i in range(a, a + k):
    print(i)
for i in range(b - k + 1, b + 1):
    print(i)

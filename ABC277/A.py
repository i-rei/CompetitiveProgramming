n, x = map(int, input().split())
p = list(map(int, input().split()))
for i, v in enumerate(p):
    if v == x:
        print(i + 1)

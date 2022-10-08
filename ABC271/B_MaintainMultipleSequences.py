n, q = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(q):
    s, k = map(int, input().split())
    print(a[s - 1][k])

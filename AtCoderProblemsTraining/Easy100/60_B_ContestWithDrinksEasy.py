n = int(input())
t = list(map(int, input().split()))
m = int(input())
for i in range(m):
    p, x = map(int, input().split())
    tt = t[:]
    tt[p - 1] = x
    print(sum(tt))

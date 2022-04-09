n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
r = [0] * n
for i, v in enumerate(h):
    r[i] = abs((t - v * 0.006) - a)
print(r.index(min(r)) + 1)

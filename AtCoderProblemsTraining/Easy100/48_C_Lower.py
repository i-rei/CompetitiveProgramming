n = int(input())
h = list(map(int, input().split()))
d = [0 if h[i + 1] - h[i] <= 0 else 1 for i in range(n - 1)]
r = 0
m = 0
for k in d:
    if k == 0:
        r += 1
    else:
        m = max(m, r)
        r = 0
print(max(m, r))

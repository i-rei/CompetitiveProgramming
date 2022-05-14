h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0
for i in range(1, h + 1):
    for k in range(1, w + 1):
        if abs(i - r) + abs(k - c) == 1:
            ans += 1
print(ans)

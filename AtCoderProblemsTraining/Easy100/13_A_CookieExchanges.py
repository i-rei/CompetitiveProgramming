a, b, c = map(int, input().split())
ans = 0
if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    print(0)
    exit()
if a == b == c:
    print(-1)
    exit()
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    half = [a // 2, b // 2, c // 2]
    a = half[1] + half[2]
    b = half[0] + half[2]
    c = half[0] + half[1]
    ans += 1
print(ans)

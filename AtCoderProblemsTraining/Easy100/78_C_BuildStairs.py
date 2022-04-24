# ユーザー解説参考
n = int(input())
h = list(map(int, input().split()))
for i in range(n - 1, 0, -1):
    l, r = h[i - 1], h[i]
    if l - r == 1:
        h[i - 1] -= 1
    elif l > r:
        print("No")
        exit()
    else:
        pass
print("Yes")

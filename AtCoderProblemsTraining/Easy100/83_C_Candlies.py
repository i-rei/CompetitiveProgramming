n = int(input())
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
dp = [[0] * n] * 2
for i in range(2):
    for j in range(n):
        if i == 0:
            if j == 0:
                dp[i][j] = a[i][j]
            else:
                dp[i][j] = dp[i][j - 1] + a[i][j]
        else:
            if j == 0:
                dp[i][j] = dp[i - 1][j] + a[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a[i][j]
print(dp[1][n - 1])

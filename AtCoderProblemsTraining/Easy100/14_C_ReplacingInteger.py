# 参考　https://tamlog.hateblo.jp/entry/2021/07/20/011230
n, k = map(int, input().split())
a = n // k
print(min(n - a * k, abs((n - a * k) - k)))

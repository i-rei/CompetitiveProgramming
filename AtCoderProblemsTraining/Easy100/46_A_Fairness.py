# 参考　https://31536000.hatenablog.com/entry/2018/05/21/014635
a, b, c, k = map(int, input().split())
if k % 2 == 0:
    print(a - b)
else:
    print((a - b) * -1)

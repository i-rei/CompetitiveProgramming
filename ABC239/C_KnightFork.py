# 参考：https://atcoder.jp/contests/abc239/editorial/3403
x1, y1, x2, y2 = map(int, input().split())
m = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
for i in m:
    for j in m:
        if x1 + i[0] == x2 + j[0] and y1 + i[1] == y2 + j[1]:
            print("Yes")
            exit()
print("No")

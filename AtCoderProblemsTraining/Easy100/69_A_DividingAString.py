#参考 https://atcoder.jp/contests/agc037/submissions/30999662
s = list(input())
a = ""
k = 0
r = 0
for i in s:
    a += i
    if k != a:
        k = a
        a = ""
        r += 1
print(r)

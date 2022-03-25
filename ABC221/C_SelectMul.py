# 参考
# https://negibose.com/abc221/#toc3(解説)
# https://qiita.com/gogotealove/items/11f9e83218926211083a(bit全検索)
# https://www.headboost.jp/python-operators/#5(ビット演算子)
n = list(input())
r = 0
for i in range(2 ** len(n)):
    a, b = [], []
    for _ in range(len(n)):
        if i >> _ & 1 == 1:
            a.append(n[_])
        else:
            b.append(n[_])
    a.sort(reverse=True)
    b.sort(reverse=True)
    if len(a) != 0 and len(b) != 0:
        c = int("".join(a)) * int("".join(b))
        r = max(r, c)
print(r)

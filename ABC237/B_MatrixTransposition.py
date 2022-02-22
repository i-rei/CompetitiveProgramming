cal, row = map(int, input().split())
a = [input().split() for i in range(cal)]
b = [0] * row
for i in range(row):
    s = [a[j][i] for j in range(cal)]
    b[i] = " ".join(s)
[print(i) for i in b]

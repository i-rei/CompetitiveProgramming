a = [int(input()) for i in range(5)]
b = [i % 10 if i % 10 != 0 else 10 for i in a]
fi = a[b.index(min(b))]
del a[b.index(min(b))]
r = 0
for i in a:
    if i % 10 == 0:
        r += i
    else:
        r += i + 10 - i % 10
print(r + fi)

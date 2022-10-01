n = int(input())
n2 = list(bin(n))[2:]
ln2 = len(n2)
a = [i for i, v in enumerate(n2) if v == '1']
la = len(a)
ans = []
for i in range(2 ** la):
    c = ['0'] * ln2
    for k in range(la):
        if ((i >> k) & 1):
            c[a[k]] = '1'
    x = int(''.join(c), 2)
    if x <= n:
        ans.append(x)
ans.sort()
for i in ans:
    print(i)

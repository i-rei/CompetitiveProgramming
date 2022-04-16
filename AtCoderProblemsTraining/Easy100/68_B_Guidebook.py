n = int(input())
r = [0] * n
for i in range(n):
    a, b = input().split()
    r[i] = [i, a, int(b)]
r = sorted(r, key=lambda x: (x[1], x[2]))
print(r)
for i in r:
    print(i[0])

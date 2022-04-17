n = input()
s = 10 ** (len(n) - 1)
k = int(n[0]) * s
a = k + s - 1
if a > int(n):
    a -= s
print(sum(list(map(int, str(a)))))

n = int(input()) + 1
a = list(map(int, input().split()))
a.insert(0, 0)
b = []
b = [sum(a[0:i + 1]) % 360 for i in range(n)]
b.sort()
b.append(360)
c = [b[i + 1] - b[i] for i in range(n)]
print(max(c))

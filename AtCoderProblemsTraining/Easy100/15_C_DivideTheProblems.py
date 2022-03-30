n = int(input())
d = sorted(list(map(int, input().split())))
s = [d[n // 2 - 1], d[n // 2]]
print(s[1] - s[0])

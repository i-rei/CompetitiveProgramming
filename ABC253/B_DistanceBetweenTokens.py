h, w = map(int, input().split())
l = []
for i in range(h):
    a = list(input())
    for k, v in enumerate(a):
        if v == "o":
            l.append([i, k])
print(abs(l[0][0] - l[1][0]) + abs(l[0][1] - l[1][1]))

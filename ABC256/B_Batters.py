n = int(input())
a = list(map(int, input().split()))
p = 0
m = [0, 0, 0, 0]
for i in a:
    m[0] = 1
    for k, v in enumerate(reversed(m)):
        if v == 1:
            if 3 - k + i <= 3:
                m[3 - k + i] = 1
                m[3 - k] = 0
            else:
                m[3 - k] = 0
                p += 1
print(p)

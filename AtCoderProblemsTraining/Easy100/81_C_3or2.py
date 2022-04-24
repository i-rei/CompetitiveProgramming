n = int(input())
a = list(map(int, input().split()))
r = 0
for i in a:
    if i % 2 == 0:
        c = 0
        while i % 2 == 0:
            i /= 2
            c += 1
        r += c
print(r)

n = int(input())
s = tuple(map(int, input().split()))
r = 0

for i in s:
    c = False
    for a in range(1, i + 1):
        for b in range(1, i + 1):
            if 4 * a * b + 3 * a + 3 * b == i:
                c = True
                break
    if not c:
        r += 1
print(r)

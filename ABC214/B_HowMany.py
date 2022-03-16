s, t = map(int, input().split())
r = 0
for a in range(s + 1):
    for b in range(s + 1 - a):
        for c in range(s + 1 - a - b):
            if a * b * c <= t:
                r += 1
print(r)

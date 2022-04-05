s = list(input())
r1, r2 = 0, 0
for i, v in enumerate(s):
    if i % 2 == 0 and v == "1":
        r1 += 1
    if i % 2 == 1 and v == "0":
        r1 += 1
    if i % 2 == 0 and v == "0":
        r2 += 1
    if i % 2 == 1 and v == "1":
        r2 += 1
print(min(r1, r2))

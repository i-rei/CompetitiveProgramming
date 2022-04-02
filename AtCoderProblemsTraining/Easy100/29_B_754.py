s = list(input())
r = 753
for i in range(len(s) - 2):
    c = int("".join(s[i: i + 3]))
    r = min(r, abs(753 - c))
print(r)

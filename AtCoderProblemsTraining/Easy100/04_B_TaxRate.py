import math
n = int(input())
for i in range(1, n + 1):
    r = math.floor(i * 1.08)
    if r == n:
        print(i)
        exit()
print(":(")

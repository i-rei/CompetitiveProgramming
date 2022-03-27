n = int(input())
x = list(map(int, input().split()))
r = 0
for i in range(1, 101):
    if i == 1:
        r = sum([(a - i) ** 2 for a in x])
    else:
        r = min(r, sum([(a - i) ** 2 for a in x]))
print(r)

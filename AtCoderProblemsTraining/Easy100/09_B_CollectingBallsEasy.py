n = int(input())
k = int(input())
x = list(map(int, input().split()))
r = 0
for i in x:
    if i < abs(k - i):
        r += i * 2
    else:
        r += abs(k - i) * 2
print(r)

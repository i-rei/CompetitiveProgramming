n = int(input())
a = list(map(int, input().split()))
x = sum(a)
y = 0
r = 10 ** 18
for i in a:
    y += i
    x -= i
    r = min(r, abs(x - y))
print(r)

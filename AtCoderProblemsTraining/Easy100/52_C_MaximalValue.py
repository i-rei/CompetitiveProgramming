n = int(input())
b = list(map(int, input().split()))
r = 0
for i in range(n - 2):
    r += min(b[i], b[i + 1])
print(r + b[0] + b[-1])

n = int(input())
x = list(map(int, input().split()))
y = [i for i in range(1, n + 1) for k in range(4)]
print(sum(y) - sum(x))

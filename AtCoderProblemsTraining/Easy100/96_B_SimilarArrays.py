import math
n = int(input())
a = list(map(int, input().split()))
x = [2 if i % 2 == 0 else 1 for i in a]
print(3 ** n - math.prod(x))

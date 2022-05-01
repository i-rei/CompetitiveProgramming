import itertools
import math
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
p = list(itertools.permutations(a))
av = []
for i in p:
    d = 0
    for j in range(n - 1):
        d += math.sqrt((i[j][0] - i[j + 1][0]) ** 2 + (i[j][1] - i[j + 1][1]) ** 2)
    av.append(d)
print(sum(av) / math.factorial(n))

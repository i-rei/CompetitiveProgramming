from itertools import combinations
n, m = map(int, input().split())
a = [i for i in range(1, m + 1)]
for i in list(combinations(a, n)):
    b = list(map(str, i))
    print(" ".join(b))

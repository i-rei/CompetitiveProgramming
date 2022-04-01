import itertools
n = [i + 1 for i in range(int(input()))]
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

c = sorted(list(itertools.permutations(n)))
print(abs(c.index(p) - c.index(q)))

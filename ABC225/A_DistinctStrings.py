import itertools
s = input()
a = set(itertools.permutations(s))
print(len(a))

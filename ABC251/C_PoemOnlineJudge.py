import collections
n = int(input())
os = set()
op = collections.defaultdict()
for i in range(n):
    s, t = input().split()
    if s not in os:
        os.add(s)
        op[i + 1] = int(t)
print(max(op, key=op.get))

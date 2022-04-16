from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
a = Counter(s)
m = max(a.values())
a = sorted([k for k, v in a.items() if v == m])
for i in a:
    print(i)

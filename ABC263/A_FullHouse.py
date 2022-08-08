import collections
a = list(input().split())
b = collections.Counter(a)
b = b.values()
if max(b) == 3 and min(b) == 2:
    print("Yes")
else:
    print("No")

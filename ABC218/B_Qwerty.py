import string
a = list(map(int, input().split()))
al = list(string.ascii_lowercase)
r = [al[i - 1] for i in a]
print("".join(r))

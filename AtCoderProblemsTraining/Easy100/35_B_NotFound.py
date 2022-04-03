s = set(input())
a = set("qwertyuioplkjhgfdsazxcvbnm")
r = a - s
if len(r) == 0:
    print("None")
else:
    r = sorted(list(r))
    print(r[0])

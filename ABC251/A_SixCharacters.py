s = input()
if len(s) == 1:
    print("".join([s] * 6))
elif len(s) == 2:
    print("".join([s] * 3))
else:
    print("".join([s] * 2))

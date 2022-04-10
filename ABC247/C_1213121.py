def making(a):
    if a == 1:
        return ["1"]
    elif a == 2:
        return list("121")
    else:
        return making(a - 1) + [str(a)] + making(a - 1)


n = int(input())
print(" ".join(making(n)))

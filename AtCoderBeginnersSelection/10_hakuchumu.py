t = input()
while not t == "":
    if t[-5:] == "dream" or t[-5:] == "erase":
        t = t[:-5]
    elif t[-6:] == "eraser":
        t = t[:-6]
    elif t[-7:] == "dreamer":
        t = t[:-7]
    else:
        print("NO")
        exit()
print("YES")

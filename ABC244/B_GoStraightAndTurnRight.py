n = int(input())
t = list(input())
now = [0, 0]
d = "E"
for i in t:
    if i == "S":
        if d == "N":
            now[1] += 1
        elif d == "E":
            now[0] += 1
        elif d == "S":
            now[1] -= 1
        else:
            now[0] -= 1
    else:
        if d == "N":
            d = "E"
        elif d == "E":
            d = "S"
        elif d == "S":
            d = "W"
        else:
            d = "N"
print(now[0], now[1])

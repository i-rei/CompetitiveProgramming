h = list(bin(int(input()))[2:])
r = "1" + "0" * (len(h) - 1)
r = int(r, 2)
print(2 * r - 1)

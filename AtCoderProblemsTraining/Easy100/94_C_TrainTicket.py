n = input()
a = 3
for i in range(2 ** a):
    r = int(n[0])
    ans = n[0]
    for j in range(a):
        if ((i >> j) & 1):
            r += int(n[j + 1])
            ans = ans + "+" + n[j + 1]
        else:
            r -= int(n[j + 1])
            ans = ans + "-" + n[j + 1]
    if r == 7:
        print(ans + "=7")
        exit()

n, minN, maxN = map(int, input().split())
result = 0

for i in range(n + 1):
    if i < 10:
        if minN <= i <= maxN:
            result += i
    elif i < 100:
        a = int(str(i)[0]) + int(str(i)[1])
        if minN <= a <= maxN:
            result += i
    elif i < 1000:
        a = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
        if minN <= a <= maxN:
            result += i
    elif i < 10000:
        a = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
        if minN <= a <= maxN:
            result += i
    else:
        # a = 10000
        a = 1
        if minN <= a <= maxN:
            result += i


print(result)

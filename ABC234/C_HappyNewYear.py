# 参考：AtCoder公式解説
k = bin(int(input()))
k = list(k[2:len(k)])
r = []
for i in range(len(k)):
    if k[i] == "1":
        r.append("2")
    else:
        r.append("0")
print("".join(r))

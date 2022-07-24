n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(input())

for i in range(n):
    for k in range(1 + i, n):
        x = a[i][k]
        y = a[k][i]
        if x == y == "W" or x == y == "L":
            print("incorrect")
            exit()
        if x == "D" and y != "D":
            print("incorrect")
            exit()
        if x != "D" and y == "D":
            print("incorrect")
            exit()
print("correct")

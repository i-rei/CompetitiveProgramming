bingo = tuple(tuple(map(int, input().split())) for i in range(3))
n = int(input())
b = {int(input()) for i in range(n)}
r = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
while b:
    c = b.pop()
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == c:
                r[i][j] = 1
for i in range(3):
    if sum(r[i]) == 3:
        print("Yes")
        exit()
    elif r[0][i] == r[1][i] == r[2][i] == 1:
        print("Yes")
        exit()
if r[0][0] == r[1][1] == r[2][2] == 1 or r[0][2] == r[1][1] == r[2][0] == 1:
    print("Yes")
else:
    print("No")

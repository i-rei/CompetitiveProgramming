a, b = map(int, input().split())
A, B = [0] * 3, [0] * 3
if a == 1:
    A[0] = 1
elif a == 2:
    A[1] = 1
elif a == 4:
    A[2] = 1
elif a == 3:
    A[0], A[1] = 1, 1
elif a == 5:
    A[0], A[2] = 1, 1
elif a == 6:
    A[1], A[2] = 1, 1
elif a == 7:
    A = [1] * 3

if b == 1:
    B[0] = 1
elif b == 2:
    B[1] = 1
elif b == 4:
    B[2] = 1
elif b == 3:
    B[0], B[1] = 1, 1
elif b == 5:
    B[0], B[2] = 1, 1
elif b == 6:
    B[1], B[2] = 1, 1
elif b == 7:
    B = [1] * 3

c = [0] * 3
for i in range(3):
    if A[i] + B[i] != 0:
        c[i] = 1
print(c[0] * 1 + c[1] * 2 + c[2] * 4)

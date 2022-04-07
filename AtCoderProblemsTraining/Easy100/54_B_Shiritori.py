n = int(input())
w = [0] * n
for _ in range(n):
    w[_] = input()
if len(set(w)) != len(w):
    print("No")
    exit()
p = w[0][-1]
for i in range(1, n):
    if not p == w[i][0]:
        print("No")
        exit()
    p = w[i][-1]
print("Yes")

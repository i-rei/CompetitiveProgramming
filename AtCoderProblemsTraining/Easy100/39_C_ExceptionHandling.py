n = int(input())
a = [int(input()) for i in range(n)]
b = sorted(a)
for i in a:
    if i != b[-1]:
        print(b[-1])
    else:
        print(b[-2])

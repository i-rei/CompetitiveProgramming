import itertools
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
toN = set()
for i in range(n - 1):
    if i == 0:
        c = [[a[i], a[i + 1]], [a[i], b[i + 1]], [b[i], a[i + 1]], [b[i], b[i + 1]]]
    else:
        c = list(itertools.product(toN, [a[i + 1], b[i + 1]]))

    cc = [x for x in c if abs(x[0] - x[1]) <= k]
    if len(cc) == 0:
        print("No")
        exit()
    else:
        toN = {i[1] for i in cc}
print("Yes")

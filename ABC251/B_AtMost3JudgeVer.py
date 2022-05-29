import itertools
n, w = map(int, input().split())
cw = [0] * w
a = list(map(int, input().split()))
a = [i for i in a if i <= w]
for i in a:
    cw[i - 1] = 1
for i in range(2, 4):
    c = list(itertools.combinations(a, i))
    for x in c:
        sumx = sum(x)
        if sumx <= w and cw[sumx - 1] == 0:
            cw[sumx - 1] = 1
print(sum(cw))

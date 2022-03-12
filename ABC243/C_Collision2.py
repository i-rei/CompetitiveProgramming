import itertools
n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
s = input()
a = [i for i in itertools.combinations(p, 2)]

for i in a:
    s1 = s[p.index(i[0])]
    s2 = s[p.index(i[1])]
    if i[0][1] == i[1][1] and s1 != s2:
        if i[0][0] < i[1][0] and s1 == "R":
            print("Yes")
            exit()
        elif i[0][0] > i[1][0] and s1 == "L":
            print("Yes")
            exit()
print("No")

n, d = map(int, input().split())
p = list(map(int, input().split()))
pp = list(map(int, input().split()))
for i in pp:
    if not(i in p):
        print("No")
        exit()
    else:
        del p[p.index(i)]
print("Yes")

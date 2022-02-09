n = int(input())
a = list(input().split())
for i in range(1, n + 1):
    if not a.count(str(i)) == 4:
        print(i)
        exit()

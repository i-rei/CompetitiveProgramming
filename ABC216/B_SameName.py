n = int(input())
s = [input() for i in range(n)]
for i in s:
    if s.count(i) > 1:
        print("Yes")
        exit()
print("No")

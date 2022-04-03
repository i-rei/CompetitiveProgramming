a, b = map(int, input().split())
s = list(input())
length = a + b + 1
if len(s) == length and s[a] == "-":
    c = s[:a] + s[a + 1:]
    for i in c:
        try:
            x = int(i)
        except ValueError:
            print("No")
            exit()
else:
    print("No")
    exit()
print("Yes")

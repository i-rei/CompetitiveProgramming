n, a, b = map(int, input().split())
s = list(input())
r = 0
rh = 0
for i in s:
    if i == "a":
        if r < a + b:
            r += 1
            print("Yes")
        else:
            print("No")
    elif i == "b":
        if r < a + b and rh < b:
            r += 1
            rh += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")

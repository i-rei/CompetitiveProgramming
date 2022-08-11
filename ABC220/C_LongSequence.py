n = int(input())
a = list(map(int, input().split()))
x = int(input())
sa = sum(a)
b = x % sa
ans = ((x - b) // sa) * len(a)
while b >= 0:
    for i in a:
        b -= i
        ans += 1
        if b < 0:
            print(ans)
            exit()
print(ans)

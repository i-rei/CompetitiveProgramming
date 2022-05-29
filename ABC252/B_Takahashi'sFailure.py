n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = max(a)
ma = [i + 1 for i in range(n) if a[i] == m]
for i in b:
    if i in ma:
        print("Yes")
        exit()
print("No")

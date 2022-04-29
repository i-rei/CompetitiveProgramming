s = list(input())
k = int(input())
for i in range(len(s)):
    if s[i] != "1":
        print(s[i])
        exit()
    if i == k - 1 and len(set(s[: i + 1])) == 1:
        print(1)
        exit()

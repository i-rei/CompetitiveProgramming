a, b = input().split()
if len(a) > len(b):
    a = a[len(a) - len(b):]
elif len(a) < len(b):
    b = b[len(b) - len(a):]
for i in range(len(a)):
    if int(a[i]) + int(b[i]) >= 10:
        print("Hard")
        exit()
print("Easy")

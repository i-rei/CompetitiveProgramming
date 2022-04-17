x = int(input())
r = {1}
for i in range(1, x + 1):
    for j in range(2, x + 1):
        a = i ** j
        if a <= x:
            r.add(a)
        else:
            break
print(max(r))

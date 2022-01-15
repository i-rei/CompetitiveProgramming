n = int(input())
if n >= 42:
    print("AGC0" + str(n + 1))
elif 0 < n < 10:
    print("AGC00" + str(n))
else:
    print("AGC0" + str(n))

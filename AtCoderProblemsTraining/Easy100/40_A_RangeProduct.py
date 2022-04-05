a, b = map(int, input().split())
if a > 0:
    print("Positive")
elif a <= 0 <= b:
    print("Zero")
elif b < 0:
    if (b - a) % 2 == 0:
        print("Negative")
    else:
        print("Positive")

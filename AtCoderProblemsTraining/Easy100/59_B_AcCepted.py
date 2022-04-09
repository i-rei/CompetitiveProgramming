s = list(input())
if s[0] == "A":
    if s[2:-1].count("C") == 1:
        s.remove("A")
        s.remove("C")
        if "".join(s).islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")

n = int(input())
h = hex(n)[2:].upper()
if len(h) == 1:
    print('0' + h)
else:
    print(h)

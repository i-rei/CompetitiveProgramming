def result(text):
    print(text)
    exit()
   

x, y, z = map(int, input().split())

if x < y < z < 0:
    result(abs(x))
if x < y < 0 < z:
    result(z * 2 + abs(x))
if x < z < y < 0:
    result(-1)
if x < z < 0 < y:
    result(abs(x))
if x < 0 < y < z:
    result(abs(x))
if x < 0 < z < y:
    result(abs(x))
if y < x < 0 < z:
    result(abs(x))
if y < x < z < 0:
    result(abs(x))
if y < z < x < 0:
    result(abs(x))
if y < z < 0 < x:
    result(x)
if y < 0 < x < z:
    result(x)
if y < 0 < z < x:
    result(x)
if z < x < y < 0:
    result(-1)
if z < x < 0 < y:
    result(abs(x))
if z < y < x < 0:
    result(abs(x))
if z < y < 0 < x:
    result(x)
if z < 0 < x < y:
    result(x)
if z < 0 < y < x:
    result(abs(z) * 2 + x)
if 0 < x < y < z:
    result(x)
if 0 < x < z < y:
    result(x)
if 0 < y < x < z:
    result(-1)
if 0 < y < z < x:
    result(-1)
if 0 < z < x < y:
    print(x)
if 0 < z < y < x:
    print(x)

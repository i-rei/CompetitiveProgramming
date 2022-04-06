h, w = map(int, input().split())
p = [input() for _ in range(h)]
tb = ["#"] * (w + 2)
print("".join(tb))
for i in p:
    print("#" + i + "#")
print("".join(tb))

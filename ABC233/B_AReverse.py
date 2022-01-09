a, b = map(int, input().split())
t = input()

print(t[:a - 1] + t[::-1][len(t) - b:len(t) - a + 1] + t[b:])

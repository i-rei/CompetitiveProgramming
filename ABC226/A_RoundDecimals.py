from decimal import Decimal, ROUND_HALF_UP
x = input()
a = Decimal(x)
r = a.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
print(r)

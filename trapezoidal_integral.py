from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# -----------


h = (pi / 2) / 100
total = 0
for k in range(1, 101):
    s = (h / 2)*((sin(k - 1) * h) + (sin(k * h)))
    total += s
print(total)

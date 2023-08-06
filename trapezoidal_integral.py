import math

# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = math.pi/2
n = 100






h = b / n
total = 0
for k in range(1, n + 1):
    s = (h / 2)*((math.sin((k - 1) * h)) + (math.sin(k * h)))
    total += s
print(total)
print(type(total))

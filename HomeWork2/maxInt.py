import sys
n = sys.maxsize
x = 1
while x > 0:
    x = x * n
    print("x number equal =", x)
for x in range(n):
    x += 1
    print(x)
print(n)
import std

values = (None, None)
max_sum = 0

for a in range(-999, 999):
    for b in range(-1000, 1000):
        n = 0
        while std.is_prime(abs(n**2 + a*n + b)):
            n = n + 1
        if n > max_sum:
            max_sum = n
            values = (a,b)

print(values[0]*values[1])

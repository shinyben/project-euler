import std

sum = 0
for i in range(2,2_000_000):
    if(std.is_prime(i)):
        sum+=i
print(sum)

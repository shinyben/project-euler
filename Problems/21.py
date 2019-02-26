import std

nums = set()

for i in range(1, 10_000):
    j = std.sum(std.proper_divisors(i))
    j_n = std.sum(std.proper_divisors(j))
    if j_n == i and j != i:
        nums.add(i)
        nums.add(j)

print(nums)

print(std.sum(nums))

import std

abundant_nums = []
for i in range(1, 28123):
    if std.sum(std.proper_divisors(i)) > i:
        abundant_nums.append(i)

print(abundant_nums)

nums = set()
for num in range(1, 28123):
    i = 0
    while i < len(abundant_nums):
        j = i
        while j < len(abundant_nums):
            if j > num:
                break
            if i + j == num:
                nums.add(num)
                i += 1
                break
            j+=1
        i+=1

sum = 0
for element in nums:
    sum += element

print(sum)

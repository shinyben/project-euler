num = 1
for i in range(1, 100):
    num *= i

s = str(num)
sum = 0
for char in s:
    sum += int(char)

print(sum)

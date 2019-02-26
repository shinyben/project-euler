import std

ones = {0 : "", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", \
    7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve", \
    13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", \
    18 : "eighteen", 19 : "nineteen"}
tens = {0 : "", 1 : "ten", 2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty", 6 : "sixty", \
    7 : "seventy", 8 : "eighty", 9 : "ninety"}

def word(N):
    if N == 1000:
        return "one thousand"
    elif N >= 100:
        return word(int(N/100)) + " hundred"  + (" and " if word(N%100) != "" else "") + word(N%100)
    elif N > 19:
        return tens[int(N/10)] + ("-" if N%10 != 0 else "") + ones[N%10]
    else:
        return ones[N]

numbers = []
for i in range(1, 1001):
    numbers.append(word(i))

print(numbers)

sum = 0
for element in numbers:
    sum+=len(std.without(element, [" ", "-"]))

print(sum)

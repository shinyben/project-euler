import std

text  = open("../Problem Resources/22.txt", "r").read()
sorted = sorted(std.without(text,['"']).split(","))

print(ord("A"))

def get_score(S):
    sum = 0
    for char in S:
        sum+=ord(char) - 64
    return(sum)

sum = 0
for i in range(len(sorted)):
    sum += (i + 1) * get_score(sorted[i])

print(sum)

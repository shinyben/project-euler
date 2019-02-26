import std

tri_number = 0

i = 1
while(len(set(std.divisors(tri_number))) < 500 - 1):
    tri_number += i
    i+=1

print(tri_number)

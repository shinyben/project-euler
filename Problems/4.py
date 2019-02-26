import std

max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if i*j > max and std.is_palindrome(str(i*j)):
            max = i*j
print(max)

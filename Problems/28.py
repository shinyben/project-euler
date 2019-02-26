# to get the concentric squares to get a 1001x1001 (501)

sum = 1
current = 1
it = 0
for i in range(2,1003//2+1):
    for corner in range(1,5):
        current = current + 2*(i-1)
        sum += current
        it += 1

print(sum)

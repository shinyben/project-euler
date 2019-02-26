def next(N):
    if N%2 == 0:
        return N/2
    else:
        return 3*N + 1

max = 0
max_N = 0
for i in range(1,1_000_000):
    orig_i = i
    chain = 0
    while(next(i) != 1):
        i = next(i)
        chain += 1
    if chain > max:
        max = chain
        max_N = orig_i

print(max_N)

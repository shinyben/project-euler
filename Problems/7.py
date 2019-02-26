import std

primes = 1
N = 1
while(primes <= 10_001):
    N+=1
    if(std.is_prime(N)):
        primes+=1
print(N)

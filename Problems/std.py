import math
import re

"""
Num methods
"""
def prime_factors(N):
    """
    Returns list of N's prime factors
    """
    for i in range(2,int(math.sqrt(N)+1)):
        if N % i == 0:
            return [i] + prime_factors(N/i)
    return [int(N)]

def proper_divisors(N):
    """
    Returns list of N's divisors
    """
    out = []
    for i in range(2, N//2 + 1):
        if N%i == 0:
            out.append(i)
    return out + [1] # to get 1

def is_prime(N):
    """
    Returns True if N is prime, False else
    """
    for i in range(2,int(math.sqrt(N)+1)):
        if N % i == 0:
            return False
    return True

"""
Str methods
"""
def is_palindrome(S):
    """
    Returns True if S is a palindrome
    """
    for i in range(int(len(S)/2)):
        if S[i] != S[-1-i]:
            return False
    return True

def without(S, L):
    """
    Returns the string S without the substrings defined in L
    """
    for element in L:
        S = re.sub(element, "", S)
    return S

"""
List/set methods
"""
def sum(L):
    """
    Returns sum of elements in L
    """
    sum = 0
    for element in L:
        sum += element
    return sum

# def fib(N):
#     if N < 2:
#         return N
#     else:
#         return fib(N-1) + fib(N-2)

def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

i = 1
while(True):
    if len(str(fib(i))) == 1000:
        break
    i += 1

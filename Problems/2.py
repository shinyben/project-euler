fib = [1,1]
while(fib[-2] + fib[-1] < 4_000_000):
    fib.append(fib[-2]+fib[-1])
sum = 0
for element in fib:
    if element%2==0:
        sum += element
print(sum)

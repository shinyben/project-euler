import math

square_sum = 0
squared_sum = 0
for i in range(1,101):
    square_sum += pow(i,2)
    squared_sum += i
squared_sum = pow(squared_sum,2)
print(squared_sum - square_sum)

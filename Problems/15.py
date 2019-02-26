"""
The idea is based around the fact that at any point,
the 'turtle' (if you think of the lattice in that way)
needs to go either down (D) or right (R) to get from
the UL to BR.

In a sequence of moves, there need to be n + m moves total
(in an n x m grid). Because we are working with square grids,
this can be generalized to 2n moves total in a n x n grid.

There need to be n moves down and n moves to the right, so if we
turn the sequence of moves into a string, encoding 0 as D and 1 as R,
we would need to have n 0's and n 1's in the string.

To count the number of valid moves through a lattice, all we would
then need to do is find the number of unique valid strings containing
nothing but 0's and 1's with length 2n and containing n 0's and 1's respectively.
"""

sum = 0

grid_dim = 20

for i in range(int(grid_dim * '0' + grid_dim * '1', 2), int(grid_dim * '1' + '0' * grid_dim, 2) + 1):
    zeroes = 0
    b = bin(i)[2:]
    s = "0" * (2*grid_dim - len(b)) + b
    for char in s:
        if char == '0':
            zeroes += 1
    if zeroes == grid_dim:
        sum+=1

print(sum)

Given an integer n, find each x such that:
 - 0 <= x <= n 
 - n + x = n XOR x


where XOR denotes the bitwise XOR operator. Return the number of x's satisfying the criteria.

**Example**

n = 4

There are four values that meet the criteria:
- 4 + 0 = 4 XOR 0 = 4
- 4 + 1 = 4 XOR 1 = 5
- 4 + 2 = 4 XOR 2 = 6
- 4 + 3 = 4 XOR 3 = 7


Return 4.
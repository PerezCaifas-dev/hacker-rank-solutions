def sumXor(n):
    # Write your code here
    counter = 0

    while n > 0:
        if (n & 1) == 0:
            counter += 1
        n >>= 1

    return 2 ** counter
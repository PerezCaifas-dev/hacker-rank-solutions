def flippingBits(n):
    # Write your code here
    binary = format(n,'032b')
    negative = ''.join('1' if bit == '0' else '0' for bit in binary)
    answer = int(negative,2)
    return answer
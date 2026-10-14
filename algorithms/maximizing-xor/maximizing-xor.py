def maximizingXor(l, r):
    # Write your code here
    answer = 0
    for i in range(l,r+1):
        for j in range(i,r+1):
            xor = i^j 
            if xor > answer:
                answer = xor
    return answer 

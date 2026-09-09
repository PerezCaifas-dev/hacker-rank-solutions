def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    answer = 'YES'
    
    for i in range(0,len(A)):
        if A[i] + B[i] < k:
            answer = 'NO'
            break
    
    return answer
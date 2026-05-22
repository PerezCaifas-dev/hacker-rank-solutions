def beautifulPairs(A, B):
    # Write your code here
    beautiful = []
    array_j = []
    for i in range(0,len(A)):
        for j in range(0,len(B)):
            if j in array_j:
                continue
            if A[i] == B[j]:
                beautiful.append([i,j])
                array_j.append(j)
                break
    
    if len(beautiful) == len(A):
        return len(beautiful) - 1
    else:
        return len(beautiful) + 1
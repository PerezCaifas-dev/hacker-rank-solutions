def largestPermutation(k, arr):
    # Write your code here
    order_arr = sorted(arr,reverse=True)
    position = {}
    
    for i, value in enumerate(arr):
        position[value] = i
    if k == 0:
        return arr
    for i in range(0,len(arr)-1,1):
        if order_arr[i] != arr[i]:
            if k > 0:
                index = position[order_arr[i]]
                arr[index] = arr[i]
                arr[i] = order_arr[i]
                k -= 1
                position[order_arr[i]] = i 
                position[arr[index]] = index
                if k == 0:
                    break 
    
    return arr
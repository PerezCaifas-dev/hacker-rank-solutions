def lonelyinteger(a):
    # Write your code here
    a.sort()
    for i in range(0,len(a),2):
        if i == len(a)-1:
            return a[i]
        if a[i] != a[i+1]:
            return a[i]
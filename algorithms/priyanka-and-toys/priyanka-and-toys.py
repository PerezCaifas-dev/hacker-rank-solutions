def toys(w):
    # Write your code here
    counter = 1
    w.sort()
    minimum = w[0]
    for i in w:
        if minimum + 4 < i:
            counter += 1
            minimum = i
    
    return counter
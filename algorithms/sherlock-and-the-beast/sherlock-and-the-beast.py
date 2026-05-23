def decentNumber(n):
    # Write your code here
    answer = False
    five_counter = n 
    three_counter = 0
    if five_counter % 3 == 0:
        answer = True
    else:
        for i in range(n-1,-1,-1):
            five_counter = five_counter - 1
            three_counter = three_counter + 1
            if i == 0:
                if three_counter % 5 == 0:
                    answer = True
            else:
                if five_counter % 3 == 0 and three_counter % 5 == 0:
                    answer = True
                    break
    
    if answer:
        print(('5'*five_counter) + ('3' * three_counter))
    else:
        print(-1)
            
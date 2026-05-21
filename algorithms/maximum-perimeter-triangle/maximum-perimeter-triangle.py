def maximumPerimeterTriangle(sticks):
    # Write your code here
    answer = [-1]
    sticks.sort()
    change = False
    for i in range(len(sticks) - 1, 1, -1):
        a = sticks[i - 2]
        b = sticks[i - 1]
        c = sticks[i]

        if a + b > c:
            if len(answer) == 1:
                answer[0] = a
                answer.insert(1, b)
                answer.insert(2, c)
            else:
                if answer[2] < c:
                    change = True
                elif answer[0] < a:
                    change = True
                if change:
                    answer[0] = a
                    answer[1] = b
                    answer[2] = c
    
    return answer
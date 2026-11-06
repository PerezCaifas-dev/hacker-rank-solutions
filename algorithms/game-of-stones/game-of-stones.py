def gameOfStones(n):
    # Write your code here
    if n % 7 == 0 or n % 7 == 1:
        return 'Second'
    else:
        return 'First'
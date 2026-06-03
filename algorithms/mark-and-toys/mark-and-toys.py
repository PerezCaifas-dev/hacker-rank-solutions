def maximumToys(prices, k):
    # Write your code here
    prices.sort() 
    total = 0
    for price in prices:
        if k >= price:
            total += 1
            k -= price
        else:
            break
    
    return total
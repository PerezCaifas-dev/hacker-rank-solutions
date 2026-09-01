def jimOrders(orders):
    # Write your code here
    count = 1
    dictionary = {}
    orderedValues = []
    for key, value in orders:
        total = key + value 
        dictionary[count] = total 
        count += 1
        orderedValues.append(total)
    dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1]))
    answer = list(dictionary.keys())
    return answer
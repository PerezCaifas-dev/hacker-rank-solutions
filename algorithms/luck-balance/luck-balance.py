def luckBalance(k, contests):
    contests.sort(key=lambda  x:x[0])
    count = k
    total = 0
    important = sum(1 for x in contests if x[1] == 1)
    for contest in contests:
        if contest[1] == 0:
            total += contest[0]
        else: 
            if count < important:
                total -= contest[0]
                count += 1
            else:
                total += contest[0] 
    return total
def addTwoNumbers(l1, l2):
    lenl1, lenl2 = len(l1), len(l2)
    print(lenl1)
    print(lenl2)
    lenmin, lenmax = min(lenl1, lenl2) , max(lenl1, lenl2)
    ret = []
    if lenl1 < lenl2:
        l1, l2 = l2, l1

    for i in range(0, lenmin):
        l1[i] = l1[i] + l2[i]
        if l1[i] + l2[i] >= 10:
            l1[i+1] = l1[i+1]+1
    for i in range(lenmin, lenmax-1):
        if l1[i]  >= 10:
            l1[i+1] = l1[i+1]+1
    if l1[lenmax-1] >= 10:
        l1.append(1)
    for j in range(0, len(l1)):
        ret.append(l1[j] % 10)
    return ret




    # for i in range(0, lenmin):
    #     if l1[i] + l2[i] >= 10:
    #         l1[i+1] = l1[i+1]+1
    # if l1[lenmin + 1] >= 10:
    #     l1[lenmin + 2] == l1[lenmin + 2] + 1
    # for i in range(0,lenmin)
    #     l1 = l1[i]+l2[]
    # for j in range(0, lenmax):
    #     ret.append(l1[j] % 10)
    return ret


print(addTwoNumbers([],[9,9,9,9]))
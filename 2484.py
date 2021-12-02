def money():
    varlst = sorted(list(map(int, input().split())))
    if len(set(varlst)) == 1:
        return varlst[0] * 5000 + 50000
    if len(set(varlst)) == 2:
        if varlst[1] == varlst[2]:
            return 10000 + varlst[1] * 1000
        return 2000 + (varlst[1] + varlst[2]) * 500
    if len(set(varlst)) == 3:
        for i in range(3):
            if varlst[i] == varlst[i + 1]:
                return 1000 + varlst[i]*100
    return varlst[-1] * 100


N = int(input())

print(max(money() for i in range(N)))

def pow_custom(lst):
    a = lst[0]
    b = lst[1]
    mod = lst[2]
    ret = 1
    while b:
        if b % 2 == 1 : ret = ret * a % mod

        a = a*a%mod

        b //= 2


    return ret


lst = list(map(int, input().split()))
print(pow_custom(lst))
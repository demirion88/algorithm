1, 4
2, 8
3, 12



A = int(input())

def ct(int):
    if int < 2:
        return 4
    if int >= 2:
        return ct(int-1) + 4


print(ct(A))

# A = int(input())
#
# def ct(int):
#     return 4*int
#
# print(ct(A))


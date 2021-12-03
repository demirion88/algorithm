
A = int(input())

def counter(A):
    ans1 = A // 5
    ans2 = 0
    if A % 5 > 0:
        ans2 = 1
    return ans1 + ans2

print(counter(A))
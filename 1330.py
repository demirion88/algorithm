A, B = map(int,input().split())

def x(A, B):
    ret = "=="
    if A > B:
        ret = ">"
    if A < B:
        ret = "<"

    return ret

print(x(A, B))


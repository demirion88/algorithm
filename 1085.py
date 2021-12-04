A, B, C, D = map(int,input().split())

#0.0 으로부터 거리의 비율을 계산
def absolutecal(int1, int2):
    if 0.5 <= (int1 / int2):
        ret = (int2 - int1)
    else:
        ret = int1
    return ret

print(min(absolutecal(A,C), absolutecal(B,D)))









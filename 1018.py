import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

# 보드의 종류를 선택한다
# --> 화이트보드(1.1) 이 화이트, 블랙보드(1.1)이 블랙
#white = list(['W','B','W','B','W','B','W','B'])
#black = list(['B','W','B','W','B','W','B','W'])
whiteboard = [["B" for j in range(8)] for i in range(8)]
blackboard = [["W" for j in range(8)] for i in range(8)]
newboard = [["A" for _ in range(m)] for i in range(n)]
for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        blackboard[i][j] = "B"
        whiteboard[i][j] = "W"
for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        blackboard[i][j] = "B"
        whiteboard[i][j] = "W"

# 받기

A = list(sys.stdin.readline().rstrip() for _ in range(n))
# A 를 배열화 해야 한다.
# 배열화 한 A를 newboard에 저장
for i in range(n):
    for j in range(m):
        newboard[i][j] = A[i][j]

#시작좌표리스트 추출하기
# 9 , 23 이면



kbmin=9999
kwmin=9999
for ki in range(0, m-7):
    for kj in range(0, n-7):
        kb = 0
        kw = 0
        for i in range(8):
            for j in range(8):
                if newboard[i + kj][j + ki] != blackboard[i][j]:
                    kb += 1
                if newboard[i + kj][j + ki] != whiteboard[i][j]:
                    kw += 1

        kbmin = min(kb, kbmin)
        kwmin = min(kw, kwmin)




print(min(kbmin, kwmin))









# NM 에서 선택 가능한 가짓수들을 표기한다
# ex) 10.10이면 N 은 1~3, M도 1~3

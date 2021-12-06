#펠린드롭수
# 숫자를 앞에서, 뒤에서 읽어도 똑같으면 펠린드롭 수이다.
#import sys
#m = list(map(str, sys.stdin.readline().rstrip().split("\n")))
def computer(var1):
    A = str(var1)
    if var1 == 0:
        pass
    elif str(A) == str(A)[-1::-1]:
        print("yes")
    else:
        print("no")

while True:
    A = input()
    if int(A) == 0:
        break
    else:
        computer(A)


# 컴퓨터는 컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. 예를 들어서 컴퓨터가 5, 2, 3을 뽑을 수도 있고
# 6, 7, 4를 뽑을 수도 있는 거죠.
# 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야 합니다.
# 컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.
# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
# 예를 들어 컴퓨터가 1, 2, 3을 뽑았다고 가정합시다. 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
# 기회는 무제한입니다. 하지만 몇 번의 시도 끝에 맞췄는지 기록됩니다.
# 3S(숫자 3개의 값과 위치를 모두 맞춘 경우)가 나오면 게임이 끝납니다.
# 진행 방식
# "0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다."가 출력됩니다.
# "숫자 3개를 하나씩 차례대로 입력하세요."가 출력됩니다.
# "1번째 숫자를 입력하세요: "가 출력되고, 사용자로부터 입력을 받습니다. 마찬가지로 "2번째 숫자를 입력하세요: "와 "3번째 숫자를 입력하세요: "가 출력되고, 사용자로부터 각각 입력을 받습니다. 만약 사용자가 중복되는 숫자를 입력하거나 범위에서 벗어나는 숫자를 입력하면, 사용자로부터 입력을 다시 받습니다.
# 사용자가 올바르게 숫자 3개를 입력하면, 규칙에 따라 "*S *B"가 출력됩니다.
# 3S가 아닌 경우, 2번부터 다시 진행합니다.
# 사용자가 3S를 달성하면, "축하합니다. *번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다."가 출력됩니다. 그리고 게임은 종료됩니다.
import random
#컴퓨터가 내는 랜덤한 3개의 변수 정의

ANSWER = []
question = []
while len(ANSWER) < 3:
    a = random.randint(1, 9)
    if a not in ANSWER:
        ANSWER.append(a)
    if a in ANSWER:
        continue

def questionmaker():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    qmi = 1
    while len(question) < 3:
        A = input(f"{qmi}번째 숫자를 입력하세요: ")
        if A == "" or A == " ":
            continue
        if int(A) in question or int(A) > 9 or int(A) < 0:
            continue
        if int(A) not in question:
            question.append(int(A))
            qmi += 1

    return question



#ball 숫자 갯수만 맞춰주는 함수,
def ball(list_1,list_2):
    i = 0
    for b in list_1:
        if b in list_2:
            i += 1
        else:
            continue
    return i

def strike(list_1,list_2):
    i = 0
    j = 0
    for j in range(0, 3):
        if list_1[j] == list_2[j]:
            i += 1
        else:
            continue
    return i


print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다")



count = 0
s = 0
while True:
    count += 1
    question = questionmaker()
    b = ball(question, ANSWER)
    s = strike(question, ANSWER)
    if s != 3:
        print(f"{s}S {b-s}B")
        question = []
    if s == 3:
        print(f"축하합니다. {count}번 만에 숫자를 맞췄습니다")
        break

#if s == 3:






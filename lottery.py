import random

def generate_numbers(n):
    b = []
    while len(b) < 6:
        a = random.randint(1, 45)
        if a not in b:
            b.append(a)
        if a in b:
            continue
    return b

def draw_winning_numbers():
    b = generate_numbers(6)
    b.sort()
    while len(b) < 7:
        a = random.randint(1, 45)
        if a not in b:
            b.append(a)
        if a in b:
            continue
    return b

def count_matching_numbers(list1, list2):
    a = 0
    for i in list1:
        if i in list2[0:5]:
            a += 1
    return a

def check(numbers, winning_numbers):
    if count_matching_numbers(numbers, winning_numbers) == 6 and winning_numbers[6] not in numbers:
        return 100000000
    if count_matching_numbers(numbers, winning_numbers) == 5 and winning_numbers[6] in numbers:
        return 50000000
    if count_matching_numbers(numbers, winning_numbers) == 5 and winning_numbers[6] not in numbers:
        return 1000000
    if count_matching_numbers(numbers, winning_numbers) == 4 and winning_numbers[6] not in numbers:
        return 50000
    if count_matching_numbers(numbers, winning_numbers) == 3 and winning_numbers[6] not in numbers:
        return 5000
    else:
        return 0


# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)




print(check([1,2,3,4,5,45],[1,2,3,4,5,6,45]))



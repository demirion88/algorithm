# 단어 정렬
# 알파벳 소문자로 이루어진 N개의 단어가 입력된다.
# 길이가 짧은것부터, 길이가 같으면 사전순서대로
# first - len
# second - order

# 길이가 주어진다.
# 전체 리스트 받는다.
# 길이가 1~50인걸 팝 한다.
# 팝 한걸 정렬해서 결과에 추가한다
#결과를 리턴한다.
"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""
#
# # 정렬?
# sub = []
# N = int(input())
# for _ in range(N):
#     sub.append(input())
#
# sub = list(set(sub))
#
#
# sub.sort(key=str.lower)
# print(sub)
# sub.sort(key=len)
# print("---")
# print(sub)
#
# stranswer = str()
# for i in range(0, len(sub)):
#     stranswer += sub[i] + "\n"
# print(stranswer)
#
#

# from sys import stdin
# read = stdin.readline().rstrip()
# for _ in range(int(input())):
#     print(read)
# from sys import stdin
# lists = (stdin.readline().rstrip() for i in range(int(input())))
# print(lists)
#
# lists = set(stdin.readline().rstrip() for i in range(int(input())))
# print('\n'.join(sorted(lists, key=lambda x: (len(x), x))))



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

sub = []
ans = []
N = int(input())
for _ in range(N):
    sub.append(input())

sub = list(set(sub))


def popAndAdd(lst):
    for i in range(1, 51):
        midans = []
        for j in range(0, len(sub)):
            if len(sub[j]) == i:
                midans.append(sub[j])
        midans.sort()
        for k in range(0,len(midans)):
            ans.append(midans[k])
    return ans

stranswer = str()
for i in range(0, len(popAndAdd(sub))):
    stranswer += popAndAdd(sub)[i] + "\n"
print(stranswer)
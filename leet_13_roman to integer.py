class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
               }
        answer = 0
        # 구간을 정해야 한다.
        # i, j 를 구하는데, dict[s[i]] < dict[s[i+1] 인 경우, 구간 시작, 구간종료를 다음시작점으로
        i = 0
        while True:
            if i > len(s) -1:
                break
            if i == len(s)-1:
                answer += dict[s[-1]]
                break
            if i < len(s) -1:
                if dict[s[i]] >= dict[s[i+1]]:
                    answer += dict[s[i]]
                    i += 1
                else:
                    answer = answer + dict[s[i+1]] - dict[s[i]]
                    i += 2 
        return answer
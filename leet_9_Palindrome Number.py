class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        lens = len(s)
        # s[0~len] vs [s[len::-1]] 비교
        if s[0:len(s)] == s[len(s)::-1]:
            return True
        else:
            False



def longestPalindrome(strvar):
    # i 가 이동하면서 잰다
    longest = ""
    start = 0
    for start in range(len(strvar)):
        end = start
        while end < len(strvar) - 1:
            if strvar[end + 1] == strvar[end]:
                end += 1
            else:
                break
        extend = 0
        while (start - extend) > 0 and (end + extend) < len(strvar)-1:
            if strvar[start - extend - 1] == strvar[end + extend + 1]:
                extend += 1
            else:
                break

        if (end + extend + 1) - (start - extend) > len(longest):
            print((end + extend + 1) - (start - extend))
            longest = strvar[(start - extend):(end + extend + 1)]
        start= end + 1

    return longest

print(longestPalindrome("aaaabaaa"))



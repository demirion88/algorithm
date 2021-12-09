# def lengthOfLongestSubstring(s):
#     if len(s) <= 1:
#         return len(s)
#
#     temp = {}
#     slow = 0
#     max_count = 1
#     for i in range(len(s)):
#         print(temp, i, slow, max_count, s[i])
#
#         if s[i] in temp and temp[s[i]] >= slow:
#             max_count = max(i - slow, max_count)
#             slow = temp[s[i]] + 1
#         temp[s[i]] = i
#     return max(len(s) - slow, max_count)
#
# a = str(input())
# print(lengthOfLongestSubstring(a))

def lengthOfLongestSubstring(s: str):
    if len(s) <= 1:
        return len(s)

    cache = {}
    base = 0
    value = 1
    for i in range(len(s)):
        if s[i] in cache and cache[s[i]] >= base:
            value = max(value, i - base)
            base = cache[s[i]] + 1
        cache[s[i]] = i
        print(f"i : {i}, s[i] : {s[i]}, value :{value},base: {base},cache: {cache}")

    return max(len(s) - base, value)

print(lengthOfLongestSubstring("acdcacbe"))
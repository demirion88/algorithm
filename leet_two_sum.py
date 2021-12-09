
def twoSum(nums, target):
    lenofnums = len(nums)
    for i in range(0, lenofnums - 1):
        for j in range(i + 1, lenofnums):
            if (sortedNums[i] + sortedNums[j]) == target:
                return i, j



import statistics

nums1 = [1,2]
nums2 = [3,4]

list1 = nums1 + nums2
nums3 = sorted(list1)
if len(nums3) % 2 != 0:
    print(nums3[len(nums3) // 2])
if len(nums3) % 2 == 0:
    A = int(len(nums3) / 2)
    B = int((len(nums3) / 2) - 1)
    print((nums3[A] + nums3[B]) / 2)



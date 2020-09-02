# 75. Sort Colors (Medium)
class Solution:
    def sortColors(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0]*len(nums)
        zero = 0
        one = 0
        for i in nums:
            if i == 0:
                zero += 1
            if i == 1:
                one += 1
        _zero = 0
        _one = zero
        _two = zero + one
        for i in range(len(nums)):
            if nums[i] == 0:
                a[_zero] = 0
                _zero += 1
            elif nums[i] == 1:
                a[_one] = 1
                _one += 1
            elif nums[i] == 2:
                a[_two] = 2
                _two += 1
        for i in range(len(a)):
            nums[i] = a[i]
        print(nums)
Solution.sortColors([2,0,2,1,1,0])
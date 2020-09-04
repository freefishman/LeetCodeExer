# 665. Non-decreasing Array (Easy)
class Solution:
    def checkPossibility(nums) -> bool:
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if flag:
                    return False
                else:
                    flag = True
                if i-2 >= 0 and i+1 <= len(nums)-1:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
        return True
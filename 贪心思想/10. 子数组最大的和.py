# 53. Maximum Subarray (Easy)
class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[:n // 2])
            max_right = self.maxSubArray(nums[n // 2:])

        maxl = nums[n // 2 - 1]
        tmp = 0
        for i in range(n // 2 - 1, -1, -1):
            tmp = tmp + nums[i]
            maxl = max(maxl, tmp)
        maxr = nums[n // 2]
        tmp = 0
        for i in range(n // 2, len(nums)):
            tmp = tmp + nums[i]
            maxr = max(maxr, tmp)
        return max(max_left, max_right, maxl + maxr)
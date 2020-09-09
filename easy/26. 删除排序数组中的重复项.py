class Solution:
    def removeDuplicates(nums) -> int:
        i = 0
        j = 0
        for _ in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return i + 1


nums = [0,0,1,1,1,2,2,3,3,4]
len = Solution.removeDuplicates(nums)
i = 0
while i < len:
    print(nums[i])
    i += 1
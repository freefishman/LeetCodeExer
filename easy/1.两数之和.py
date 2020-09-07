class Solution:
    def twoSum(nums, target):
        res = []
        for i in range(len(nums)):
            if target-nums[i] in nums:
                if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):
                    continue
                else:
                    j = nums.index(target - nums[i],i+1)
                    if nums[i] + nums[j] == target:
                        res.append(i)
                        res.append(j)
                        break
        return res

print(Solution.twoSum([3,3],6))
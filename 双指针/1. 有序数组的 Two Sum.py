# 167. Two Sum II - Input array is sorted (Easy)
class Solution:
    def twoSum(numbers, target):
        # 超时
        # res = []
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             res.append(i+1)
        #             res.append(j+1)
        #             return res
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
print(Solution.twoSum([5,25,75],100))
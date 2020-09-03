# 435. Non-overlapping Intervals (Medium)
# class Solution:
#     def eraseOverlapIntervals(intervals) -> int:
#         length = len(intervals)
#         intervals = sorted(intervals,key=lambda item:item[0])
#         intervals = sorted(intervals,key=lambda item:item[1])
#         i = 0
#         while i <= len(intervals) - 2:
#             if len(intervals) - 1 > 0 and intervals[i][0] == intervals[i+1][0]:
#                 intervals = intervals[:i+1] + intervals[i+2:]
#                 i = 0
#             elif intervals[i][1] > intervals[i+1][0]:
#                 intervals = intervals[:i + 1] + intervals[i + 2:]
#                 i = 0
#             else:
#                 i += 1
#         return length - len(intervals)
# class Solution:
#     def eraseOverlapIntervals(intervals) -> int:
#         n = len(intervals)
#         if n == 0:
#             return 0
#         dp = [1] * n
#         intervals.sort(key = lambda a:a[1])
#
#         for i in range(len(intervals)):
#             for j in range(i-1, -1, -1):
#                 if intervals[i][0] >= intervals[j][1]:
#                     dp[i] = max(dp[i], dp[j]+1)
#                     break
#             dp[i] = max(dp[i], dp[i-1])
#         return n - max(dp)
#
# print(Solution.eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))


# 300. 最长上升子序列
import bisect
class Solution:
    def lengthOfLIS(nums) -> int:
        if len(nums) == 0:
            return 0
        a = [nums[0]]
        for i in range(len(nums)):
            if nums[i] > a[len(a) - 1]:
                a.append(nums[i])
            else:
                left = 0
                right = len(a) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if mid == 0:
                        if a[mid] < nums[i]:
                            a[mid + 1] = nums[i]
                        else:
                            a[mid] = nums[i]
                        break
                    if a[mid - 1] <= nums[i] <= a[mid]:
                        a[mid] = nums[i]
                        break
                    if a[mid] > nums[i]:
                        right = mid
                    elif a[mid] < nums[i]:
                        left = mid + 1
        return len(a)


        # if len(nums) == 0:
        #     return 0
        # a = []
        # for i in nums:
        #     n = bisect.bisect_left(a, i)
        #     a[n:n+1] = [i]
        # return len(a)


#         if len(nums) == 0:
#             return 0
#         dp = [1] * len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)

# class Solution:
#     def lengthOfLIS(nums) -> int:
#         if len(nums) == 0:
#             return 0
#         a = [nums[0]]
#         for i in range(0, len(nums)):
#             if nums[i] > a[len(a) - 1]:
#                 a.append(nums[i])
#             else:
#                 for j in range(len(a) - 1, -1, -1):
#                     if j == 0:
#                         a[j] = nums[i]
#                     if a[j] >= nums[i] > a[j - 1]:
#                         a[j] = nums[i]
#                         break
#         return len(a)
# print(Solution.lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(Solution.lengthOfLIS([10,9,2,5,3,4]))
# print(Solution.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(Solution.lengthOfLIS([2,15,3,7,8,6,18]))


# 646. 最长数对链
# class Solution:
#     def findLongestChain(pairs) -> int:
#         if len(pairs) == 0:
#             return 0
#         dp = [1] * len(pairs)
#         pairs = sorted(pairs, key = lambda a:a[0])
#         for i in range(len(pairs)):
#             for j in range(i-1, -1, -1):
#                 if pairs[j][1] < pairs[i][0]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     break
#         return max(dp)


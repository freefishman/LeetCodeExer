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
# class Solution:
#     def lengthOfLIS(nums) -> int:
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
# print(Solution.lengthOfLIS([2,15,3,7,8,6,18]))


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

# 452. 用最少数量的箭引爆气球
class Solution:
    def findMinArrowShots(points) -> int:
        # if len(points) == 0:
        #     return 0
        # dp = [1] * len(points)
        # points = sorted(points, key = lambda a : a[1])
        # for i in range(len(points)):
        #     for j in range(0, i):
        #         if points[i][0] > points[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)
        if len(points) <= 1: return len(points)
        ## 根据区间右端点排序
        points = sorted(points, key=lambda x: x[1])
        arrow = 1
        new_point = points[0][1]
        for point in points[1:]:
            if point[0] > new_point:  # 如果区间不重叠，更新new_point且射箭数量+1
                new_point = point[1]
                arrow += 1
        return arrow


print(Solution.findMinArrowShots([[60051528,100384399],[12805732,32854561],[78409503,93939522],[13258270,86621638],[9959708,87446423],[73226340,104744489],[747796,90448519],[17142618,85144863],[50122846,89616297],[90892921,151136476]]))
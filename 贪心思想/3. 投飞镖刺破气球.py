# 452. Minimum Number of Arrows to Burst Balloons (Medium)
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
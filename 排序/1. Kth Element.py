# 215. 数组中的第K个最大元素(Medium)
import heapq
import random
class Solution:
    def findKthLargest(nums, k) -> int:
        # sort()方法的时间复杂度为O(N * logN), 空间复杂度为O(1)
        # nums.sort()
        # return nums[-k]

        #小顶堆
        # heap = []
        # heapq.heapify(heap)
        # for i in nums:
        #     heapq.heappush(heap, i)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return heap[0]

        # 快排分区_讨论区elevenxx的解法
        def partition(left, right, pivot_idx):
            pivot_value = nums[pivot_idx]
            new = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[i], nums[new] = nums[new], nums[i]
                    new += 1
            nums[new], nums[right] = nums[right], nums[new]
            return new

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new = partition(left, right, pivot_idx)
            if new == k - 1:
                return nums[new]
            elif new > k - 1:
                right = new - 1
            else:
                left = new + 1
print(Solution.findKthLargest([3,2,1,5,6,4],2))
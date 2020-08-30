# 88. Merge Sorted Array (Easy)
class Solution:
    def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        l = m+n-1
        while l>=0:
            if i < 0:
                nums1[:l+1] = nums2[:j+1]
                break
            elif j < 0:
                nums1[:l+1] = nums1[:i+1]
                break
            if nums1[i] >= nums2[j]:
                nums1[l] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[l] = nums2[j]
                j -= 1
            l -= 1
        print(nums1)
Solution.merge([1,2,3,0,0,0],3,[2,5,6],3)

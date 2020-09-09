class Solution(object):
    def longestCommonPrefix(strs):
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans

print(Solution.longestCommonPrefix(["flower","flow","flight"]))
class Solution:
    def strStr(haystack: str, needle: str) -> int:
        if len(needle)==0 and len(haystack) != 0:
            return 0
        if len(haystack)==0:
            if len(needle)!=0:
                return -1
            else:
                return 0
        for i in range(len(haystack)):
            index = haystack[i:].find(needle)
            if index:
                return index
            if i == len(haystack) - 1:
                return -1

print(Solution.strStr('a','a'))
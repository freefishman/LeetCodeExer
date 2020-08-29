# 680. Valid Palindrome II (Easy)
class Solution:
    def validPalindrome(s: str) -> bool:
        i = 0
        j = len(s)-1
        flag = False
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j] and not flag:
                if s[i+1] == s[j]:
                    i += 1
                elif s[i] == s[j-1]:
                    j -= 1
                flag = True
            elif s[i] != s[j] and flag:
                return False
        return True
print(Solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
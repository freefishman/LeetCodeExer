# 392. Is Subsequence (Medium)
class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) == 1:
            for i in t:
                if s[0] == i:
                    return True
            return False
        a = 0
        b = 0
        while a != len(s) and b != len(t):
            if s[a] == t[b]:
                a += 1
                b += 1
            elif s[a] != t[b]:
                b += 1
        if a == len(s) - 1:
            return True
        else:
            return False

print(Solution.isSubsequence("abc", "ahbgdc"))
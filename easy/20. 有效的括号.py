class Solution:
    def isValid(s: str) -> bool:
        # 时间复杂度为O(n)，空间复杂度为O(n)
        d = {'(': ")", '{': "}", '[': "]"}
        stack = []
        for ch in s:
            if ch in d:
                stack.append(ch)
            elif stack:
                if ch != d[stack.pop()]:
                    return False
            else:
                return False
        return not stack


print(Solution.isValid("([)]"))
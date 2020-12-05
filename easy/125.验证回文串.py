class Solution:
    def isPalindrome(s):
        left = 0
        right = len(s)-1
        sign = [" ", ",", ".", ":", "!", "?", "@"]
        while left < right:
            if s[left] in sign:
                left += 1
                continue
            if s[right] in sign:
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                print("false")
                exit(0)
        print("true")
Solution.isPalindrome("ab@a")
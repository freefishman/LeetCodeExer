import math
class Solution:
    def plusOne(digits):
        num = ""
        while digits[:]:
            num += str(digits.pop(0))
        num = int(num) + 1
        num = str(num)
        res = []
        while num[:]:
            res.append(int(num[:1]))
            num = num[1:]
        return res

print(Solution.plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]))
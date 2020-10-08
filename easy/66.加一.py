import math
class Solution:
    def plusOne(digits):
        # num = ""
        # while digits[:]:
        #     num += str(digits.pop(0))
        # num = int(num) + 1
        # num = str(num)
        # res = []
        # while num[:]:
        #     res.append(int(num[:1]))
        #     num = num[1:]
        # return res
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] is not 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] is 0:
                    digits.insert(0, 1)
                    return digits

print(Solution.plusOne([4,3,2,9]))
# 633. Sum of Square Numbers (Easy)
import math
class Solution:
    def judgeSquareSum(c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            if i*i + j*j == c:
                return True
            elif i*i + j*j > c:
                j -= 1
            else:
                i += 1
        return False
print(Solution.judgeSquareSum(4))
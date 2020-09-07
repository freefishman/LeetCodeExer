class Solution:
    def reverse(x: int) -> int:
        s = str(abs(x))
        s = s[::-1]
        if x < 0:
            s = "-" + s
        res = int(s)
        if res >= -2**31 and res <= 2**31-1:
            return res
        else:
            return 0

Solution.reverse(-123)
class Solution:
    def convert(s, numRows):
        if numRows < 2:
            return s
        i = 0
        flag = -1
        res = ["" for _ in range(numRows)]
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return "".join(res)
print(Solution.convert("LEETCODEISHIRING",3))
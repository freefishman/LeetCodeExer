class Solution:
    def addDigits(num: int) -> int:
        res = str(num)
        tmp = 0

        while True:
            for i in res:
                tmp += int(i)
            if len(str(tmp))!=1:
                res = str(tmp)
                tmp = 0
            elif len(str(tmp))==1:
                break
        return tmp
print(Solution.addDigits(199))
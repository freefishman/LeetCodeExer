# 524. Longest Word in Dictionary through Deleting (Medium)
class Solution:
    def findLongestWord(s, d) -> str:
        # 可以用元组表示多关键字排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        d.sort(key=lambda x: [-len(x), x])
        for i in d:
            count = 0
            str_n = 0
            list_n = 0
            while True:
                if str_n > len(s) - 1 or list_n > len(i) - 1:
                    break
                if s[str_n] == i[list_n]:
                    str_n += 1
                    list_n += 1
                    count += 1
                elif s[str_n] != i[list_n]:
                    str_n += 1
                if count == len(i):
                    return i
        return ""

print(Solution.findLongestWord("apple",[]))
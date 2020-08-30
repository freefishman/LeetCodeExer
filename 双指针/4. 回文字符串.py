# 680. Valid Palindrome II (Easy)
class Solution:
    def validPalindrome(s: str):
        # "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
        # 差两个用例
        # i = 0
        # j = len(s)-1
        # flag = False
        # while i < j:
        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     elif s[i] != s[j] and not flag:
        #         if s[i+1] == s[j]:
        #             i += 1
        #         elif s[i] == s[j-1]:
        #             j -= 1
        #         flag = True
        #     elif s[i] != s[j] and flag:
        #         return False
        # return True


#         切片
#         if s == s[::-1]:
#             return True
#         i = 0
#         j = len(s) - 1
#         while i < j:
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 a = s[i + 1 : j + 1]
#                 b = s[i : j]
#                 return a == a[::-1] or b == b[::-1]

        # 递归
        def search(s, times):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    if times == 0:
                        return False
                    return search(s[i:j], times - 1) or search(s[i + 1:j + 1], times - 1)
                i += 1
                j -= 1
            return True
        print(search(s,1))
Solution.validPalindrome("aba")
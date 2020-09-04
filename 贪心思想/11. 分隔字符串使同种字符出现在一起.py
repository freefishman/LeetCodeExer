# 763. Partition Labels (Medium)
class Solution:
    def partitionLabels(S):
        dic = {v:k for k, v in enumerate(S)}
        start = 0
        end = 0
        res = []
        for i in range(len(S)):
            end = max(end, dic[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res



        # 先确定思路：看见开头一个字母，就要看这个字母最后出现在哪，然后康康这个开头和结尾之间的那些其他字母是不是都落在这个区间里，
        # 如果不是，则扩充区间，如果是，那就最好了ww。
        # 另一点是确定用什么方法，很多题你不看参考答案真的想不出来要走哪条路，倒不是说这条路有多难，而是不能确定到底应该往哪个方向去想。
        # 对于这道题，一个关键点是利用字典key的唯一性来记载一个字母最大的index是几。
        # 然后，遍历字符串并跟它比较，用max函数来康康是边界大还是当前遍历的这个字母的最大index大，
        # 如果当前遍历字母的最大index大，那就说明超过了边界，那就要更新边界，大概就是这个思路。
        # 结合我说的，康康下面的代码哈。

        # max_index = {item: idx for idx, item in enumerate(S)}  # 这样写就是一个键：一个值，然后通过遍历来更新到最大的那个index
        # start, end = 0, 0  # 起始边界， 结束边界
        # ans = []
        #
        # for idx, i in enumerate(S):
        #     end = max(end, max_index[i])  # 这里就是用边界和当前遍历到的那个字母的最大index去比较，看看谁大，
        #     # 如果最大index大就扩充边界。
        #     if idx == end:  # 最后，遍历的位置和边界重合了，那就ok了，从这里截断并记录长度。 就这些，可以再慢慢理解下。
        #         ans.append(end - start + 1)
        #         start = idx + 1
        #
        # return ans





        # res = []
        # i = 0
        # while i < len(S):
        #     k = i
        #     tmp = -1
        #     while k != -1:
        #         k = S.find(S[k], k+1)
        #         tmp = max(tmp, k)
        #     if tmp == -1:
        #         tmp = i
        #     subtmp = -1
        #     j = i + 1
        #     while j < tmp+1:
        #         subk = j
        #         while subk != -1:
        #             subk = S.find(S[subk], subk+1)
        #             subtmp = max(subtmp, subk)
        #             tmp = max(tmp, subtmp)
        #         j += 1
        #     res.append(tmp + 1 - i)
        #     i = tmp + 1
        # return res

print(Solution.partitionLabels("qiejxqfnqceocmy"))
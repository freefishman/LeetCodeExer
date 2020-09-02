# 347. Top K Frequent Elements (Medium)
class Solution:
    def topKFrequent(nums, k: int):
        # freq = {}
        # for i in nums:
        #     if i not in freq:
        #         freq[i] = 1
        #     else:
        #         freq[i] += 1
        # sorted_freq = sorted(freq.items(),key = lambda item : item[1], reverse = True)[:k]
        # res = []
        # for i in sorted_freq:
        #     res.append(i[0])
        # return res
        n_f = {}
        v_k = {}
        for i in nums:
            if i not in n_f:
                n_f[i] = 1
            else:
                n_f[i] += 1
        for v, k in n_f.items():
            if v not in v_k:
                v_k[k] = [v]
            else:
                v_k[k].append(v)
        arr = []
        for x in range(len(nums), 0, -1):
            if x in v_k:
                for i in v_k[x]:
                    arr.append(i)
        return arr[:k]

print(Solution.topKFrequent([-1,-1],2))
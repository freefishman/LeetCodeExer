class Solution:
    def climbStairs(n: int) -> int:
        # f1 = 1
        # f2 = 2
        # while n > 1:
        #     f1, f2 = f2, f1 + f2
        #     n -= 1
        # return f1

        s = [1, 1]
        while n >= len(s):
            s.append(s[-1] + s[-2])
        return s[n]

# class Solution:
#     @functools.lru_cache(100)
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         elif n >= 3:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)

a = Solution.climbStairs(5)
print(a)
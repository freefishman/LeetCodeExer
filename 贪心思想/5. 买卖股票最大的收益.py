# 121. Best Time to Buy and Sell Stock (Easy)
class Solution:
    def maxProfit(prices) -> int:
        if len(prices) <= 1:
            return 0
        miniprice = float("inf")
        maxprofit = 0
        for price in prices:
            miniprice = min(miniprice, price)
            maxprofit = max(maxprofit, price - miniprice)
        return maxprofit


# class Solution:
#     def maxProfit(self, prices) -> int:
#         if len(prices) <= 1:
#             return 0
#         interest = []
#         for i in range(len(prices)-1):
#             if max(prices[i+1:]) <= prices[i]:
#                 interest.append(0)
#             elif max(prices[i+1:]) > prices[i]:
#                 interest.append(max(prices[i+1:]) - prices[i])
#         return max(interest)
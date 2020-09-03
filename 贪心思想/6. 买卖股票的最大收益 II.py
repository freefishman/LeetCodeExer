# 122. Best Time to Buy and Sell Stock II (Easy)
class Solution:
    def maxProfit(prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
        return profit

print(Solution.maxProfit([1,2,3,4,5]))
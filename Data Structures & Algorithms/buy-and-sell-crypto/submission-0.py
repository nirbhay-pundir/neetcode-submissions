class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_difference = 0
        for i in range(size - 1):
            for j in range(i + 1, size):
                diff = prices[j] - prices[i]
                if max_difference < diff:
                    max_difference = diff
        
        return max_difference
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        buy > sell, buy = sell
        max_profit = max(sell-buy, max_proffit)
        
        don't use max when a single if stament can be used, max takes longer
        """
        buy = prices[0]
        max_profit = 0
        
        for num in prices:
            current = num - buy
            
            if buy > num:
                buy = num
                
            if current > max_profit:
                max_profit = current
        
        return max_profit

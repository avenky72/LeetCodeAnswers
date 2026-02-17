class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = max((prices[i]-buy), profit)
            
        return profit

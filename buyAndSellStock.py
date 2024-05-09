# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if j < i: 
                    break
                else:
                    if prices[j] > prices[i]:
                        if (prices[j] - prices[i]) > sell:
                            sell = (prices[j] - prices[i])
        return sell

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for change in range(1, amount+1):
            for coin in coins:
                if (change - coin) >= 0:
                    # example given coins 3 and 4: dp[7] = min(dp[7], 1+dp[7-3])
                    # the idea is to loop through all coin values minus from dp[change]
                    # and find the one that takes the minimum coins
                    # but since we can't loop through all coin values at a time, do it like this
                    dp[change] = min(dp[change], 1+dp[change-coin])
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

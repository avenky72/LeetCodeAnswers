class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mon = money
        prices.sort()
        for i in prices:
            for j in prices[i:len(prices)]:
                if (mon - (i+j)) >= 0:
                    mon -= (i+j)
                    return mon
            return mon
        return mon

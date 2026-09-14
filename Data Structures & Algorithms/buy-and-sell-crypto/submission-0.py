class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        res = 0
        for price in prices:
            tmp = price - min
            if tmp > res:
                res = tmp
            elif price < min:
                min = price
        return res
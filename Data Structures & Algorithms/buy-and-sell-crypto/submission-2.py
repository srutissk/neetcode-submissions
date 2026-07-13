class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        """
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res
        """
        # dynammic programming?
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
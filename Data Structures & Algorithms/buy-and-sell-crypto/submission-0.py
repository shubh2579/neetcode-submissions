class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpr = 0
        for i in range(len(prices)):
            if i == 0:
                lp = prices[i]
            else:
                if prices[i] < lp:
                    lp = prices[i]
            diff = prices[i] - lp
            if diff > maxpr:
                maxpr = diff
            else:
                continue
        return maxpr

        
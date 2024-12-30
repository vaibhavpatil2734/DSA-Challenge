class Solution:
    def maximumProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0
        n = len(prices)
        for i in range(1,n-1):
            minPrice = min(minPrice,prices[i])

            maxProfit = max(maxProfit,prices[i]-minPrice)
        return maxProfit





s = Solution()
prices = [7, 10, 1, 3, 6, 9, 2]
print(s.maximumProfit(prices))
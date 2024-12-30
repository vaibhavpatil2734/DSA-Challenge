class Solution:
    def maximumProfit(self, prices) -> int:

        n = len(prices)
        profit =0
        for i in range(n-1):
            if prices[i]<prices[i+1]:
                profit +=prices[i+1]-prices[i]
            
        return profit      
                    




s = Solution()
prices = [100, 180, 260, 310, 40, 535, 695]
print(s.maximumProfit(prices))
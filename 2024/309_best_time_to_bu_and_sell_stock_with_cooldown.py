class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0: return 0

        buy = -prices[0]
        sell = cooldown = 0

        for p in prices[1:]:
            buy = max(buy, cooldown - p)
            cooldown = max(cooldown, sell)
            sell = max(sell, buy + p)

        return sell
    
if __name__ == "__main__":
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
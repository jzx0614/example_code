class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0: return 0
        buy = buy2 = -prices[0]
        sell = sell2 = 0
        
        for p in prices[1:]:
            buy = max(buy, -p)
            sell = max(sell, buy + p)
            buy2 = max(buy2, sell - p)
            sell2 = max(sell2, buy2 + p)

        return max(sell, sell2)
    
if __name__ == "__main__":
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
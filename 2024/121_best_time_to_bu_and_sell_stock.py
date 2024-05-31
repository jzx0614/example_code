class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0: return 0

        buy = -prices[0]
        sell = 0
        for p in prices[1:]:
            buy = max(buy, -p)
            sell = max(sell, buy + p)

        return sell
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
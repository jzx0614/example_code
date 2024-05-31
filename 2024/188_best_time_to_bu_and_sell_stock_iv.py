class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if len(prices) == 0: return 0
        buy = [[-prices[0]] * k for i in range(len(prices))]
        sell = [[0] * k for i in range(len(prices))]

        print(sell)
        for i, p in enumerate(prices):
            if i == 0: continue
            for trans in range(k):
                buy[i][trans] = max(buy[i-1][trans], sell[i][trans - 1] - p)
                sell[i][trans] = max(sell[i-1][trans], buy[i-1][trans] + p)  

        return max(sell[-1])

    
if __name__ == "__main__":
    print(Solution().maxProfit(2, [3,3,5,0,0,3,1,4]))
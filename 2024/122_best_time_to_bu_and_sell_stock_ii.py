class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = [[0] * len(prices) for i in range(len(prices))]
        # prices[i] = max(price[i-1] + price[i], price[i])

        for i in range(len(prices)-1):      # buy  0 ~ (length-1)
            for j in range(i, len(prices)):  # sell i ~ length
                 profit[i][j] = prices[j] - prices[i]
        for i in range(len(prices)):
            print(profit[i])
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))



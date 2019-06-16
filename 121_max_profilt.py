class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = 0
        for idx in xrange(len(prices)-2, -1, -1):
            dp = max(prices[idx+1]-prices[idx], dp)
            prices[idx] = max(prices[idx], prices[idx+1])
        return dp
        
if __name__ == "__main__":
    Solution().maxProfit([7,1,5,3,6,4])
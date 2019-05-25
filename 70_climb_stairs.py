class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [1,1]
        for i in xrange(2, n+1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

if __name__ == "__main__":
    print Solution().climbStairs(3)
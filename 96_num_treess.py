class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in xrange(n)]
        
        for x in xrange(n):
            for y in xrange(n):
                i, j = y, x + y 

                if j >= n:
                    continue

                if i == j:
                    dp[i][j] = 1
                    continue

                for idx in xrange(i, j+1):
                    left = dp[i][idx-1] if i <= idx -1 else 1
                    right = dp[idx+1][j] if idx+1 <= j else 1

                    dp[i][j] += left * right

        return dp[0][-1]

if __name__ == "__main__":
    print Solution().numTrees(4)
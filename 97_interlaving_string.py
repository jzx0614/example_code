class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False
        dp = [(len(s2) + 1) * [False]  for _ in xrange(len(s1) + 1) ]
        
        dp[0][0] = True
        
        for i, c1 in enumerate(s1, 1):
            if s3[i-1] != c1: break
            dp[i][0] = True
        for i, c2 in enumerate(s2, 1):
            if s3[i-1] != c2: break
            dp[0][i] = True

        for i, c1 in enumerate(s1, 1):
            for j, c2 in enumerate(s2, 1):
                c3 = s3[i+j-1]
                dp[i][j] = (dp[i-1][j] and c1 == c3) or \
                           (dp[i][j-1] and c2 == c3)

        return dp[-1][-1]

        
if __name__ == "__main__":
    print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
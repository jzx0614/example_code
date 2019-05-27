class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [(len(word2) + 1) * [0] for _ in xrange(len(word1) + 1) ]
        dp[0][0] = 0
        for idx, _ in enumerate(word2, 1):
            dp[0][idx] = idx
        for idx, _ in enumerate(word1, 1):
            dp[idx][0] = idx

        for idx1, w1 in enumerate(word1, 1):
            for idx2, w2 in enumerate(word2, 1):
                dp[idx1][idx2] = min(dp[idx1-1][idx2] + 1 , dp[idx1][idx2-1] + 1, dp[idx1-1][idx2-1]  + (0 if w1 == w2 else 1))

        return dp[-1][-1]


if __name__ == "__main__":
    print Solution().minDistance("intention", "execution")
    print Solution().minDistance("horse", "ros")
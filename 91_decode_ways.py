class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for idx, c in enumerate(s[1:], 1):
            num1 = num2 = 0
            if c !='0':
                num1 = dp[idx-1]
            if idx >=1 and 10 <= int(s[idx-1:idx+1]) <= 26:
                num2 = 1 if idx == 1 else dp[idx-2]
            dp[idx] = num1 + num2

        return dp[-1]

if __name__ == "__main__":
    print Solution().numDecodings("10")
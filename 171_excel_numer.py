class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_map = [chr(x + ord('A')) for x in xrange(26)]
        ans = 0
        for idx, c in enumerate(s[::-1]):
            value = c_map.index(c) + 1
            ans += value * (26 ** idx)
        return ans

if __name__ == "__main__":
    print Solution().titleToNumber('BA')
        
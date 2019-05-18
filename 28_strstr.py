class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        ans_len = len(needle)
        s = needle + '$' + haystack

        z = [0] * len(s)
        z[0] = 0
        l = r = 0
        for idx in xrange(1, len(s)):
            z[idx] = max(0, min(z[idx - l], r -idx + 1))
            while( idx + z[idx] < len(s) and s[idx + z[idx]] == s[z[idx]]):
                l, r, z[idx] = idx, idx + z[idx], z[idx] + 1

                if z[idx] == ans_len:
                    return idx - ans_len -1
        return -1
        

if __name__ == "__main__":
    print Solution().strStr("hello", "ll")
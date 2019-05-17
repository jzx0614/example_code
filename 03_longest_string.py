class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        # """
        # if len(s) <= 1:
        #     return len(s)

        def getSubString(str):
            curr_str = ""
            for c in str:
                if c in curr_str:
                    break
                curr_str += c
            print curr_str
            return len(curr_str)

        max_len = 0
        for idx, char in enumerate(s):
            length = getSubString(s[idx:])
            max_len = max(max_len, length)
        return max_len

    def length2(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
            print usedChar
        # print usedChar
        return maxLength

if __name__ == "__main__":
    s = "abcabcbb"
    s = "bbbbbbbb"
    s = "pwwkew"
    # s = "c"
    # s = "dvdf"
    # print Solution().lengthOfLongestSubstring(s)

    print Solution().length2(s)

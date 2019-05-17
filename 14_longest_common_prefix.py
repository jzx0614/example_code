class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        min_len = min(map(lambda x:len(x), strs))
        idx = 0
        while idx < min_len:
            s = strs[0][idx]
            for i in range(1, len(strs)):
                if strs[i][idx] != s:
                    return strs[i][:idx]
            idx += 1
        return strs[0][:idx]

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["abab","aba","abc"])
    # print Solution().longestCommonPrefix(["flower","flow","flight"])
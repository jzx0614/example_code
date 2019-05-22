class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_map = {}

        for s in strs:
            str_map.setdefault(tuple(sorted(s)), []).append(s)

        return str_map.values()
if __name__ == "__main__":
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
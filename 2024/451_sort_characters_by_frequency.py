class Solution:
    def frequencySort(self, s: str) -> str:
        if (len(s) == 0):
            return ""

        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
            
        freq_list = reversed(sorted((value, key) for key, value in freq.items()))
        out_str = "".join(key * value for value, key in freq_list)
        return out_str
    
if __name__ == "__main__":
    print(Solution().frequencySort("tree"))
    print(Solution().frequencySort("Aabb"))
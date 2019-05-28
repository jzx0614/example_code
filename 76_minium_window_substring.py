class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window_list = []
        for r_idx, r_char in enumerate(s):
            if r_char not in t: continue
            window_list.append((r_idx, r_char))

        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        t_map["total"] = len(t_map)

        l = r = 0
        result = float('inf'), 0, 0
        window_count = {"total": 0}

        for r, data in enumerate(window_list):
            r_idx, char = data
            window_count[char] = window_count.get(char, 0) + 1

            if window_count[char] == t_map[char]:
                window_count["total"] += 1
            
            while l <= r and window_count["total"] == t_map["total"]:
                l_idx, l_char = window_list[l]
                if  r_idx - l_idx + 1 < result[0]:
                    result = r_idx - l_idx + 1, l_idx, r_idx
                window_count[l_char] -= 1
                if window_count[l_char] < t_map[l_char]:
                    window_count["total"] -= 1
                l += 1
                 
        
        return s[result[1]:result[2]+1] if result[0] != float("inf") else ""
          
if __name__ == "__main__":
    # print Solution().minWindow("ADOBECODEBANC", "ABC")
    print Solution().minWindow("aab", "aab")
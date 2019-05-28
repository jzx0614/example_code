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

        result = float('-inf'), 0, 0


        print t_map
        print window_list
          # if select_char == total_len:
            # if result[0] 
          
if __name__ == "__main__":
    print Solution().minWindow("ADOBECODEBANC", "ABC")
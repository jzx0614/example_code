class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return self.z_function(s)
        

    def z_function(self, p_str):
        s = ','+ ','.join(p_str) + ','
        z = [0] * len(s)
        z[0] = 1
        j = 0
        r_idx = 0
        max_idx = 0
        for i in xrange(1, len(s)):
            ii = j - (i - j)
            z[i] = max(1, min(z[ii], r_idx - i + 1))

            while(i + z[i] < len(s) 
                and i - z[i] >= 0 
                and s[i + z[i]] == s[i - z[i]]):
                j = i 
                r_idx = i + z[i] 
                z[i] += 1
        max_range = max(z)
        max_index = z.index(max_range)
        return filter(lambda x:x!=',', s[max_index-max_range+1:max_index+max_range-1])
        
if __name__ == "__main__":
    print Solution().longestPalindrome('abaabaab')
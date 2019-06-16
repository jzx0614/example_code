class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1

        while l < r:
            if not s[l].isalnum(): 
                l += 1
                continue
            if not s[r].isalnum(): 
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

if __name__ == "__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
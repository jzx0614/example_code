class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        for i in range(len(x_str)/2):
          if x_str[i] != x_str[-(i+1)]:
            return False
        return True
        
if __name__ == "__main__":
    print Solution().isPalindrome(121)
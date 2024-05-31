class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.is_palindrome(s, 0, len(s) - 1, False) 
    
    def is_palindrome(self, s, left, right, used_deleted = True):
        while left < right:
            if s[left] != s[right]: 
                if used_deleted == True:
                    return False
                return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
            left, right = left + 1, right - 1
        return True
        
if __name__ == "__main__":
    print(Solution().validPalindrome(""))
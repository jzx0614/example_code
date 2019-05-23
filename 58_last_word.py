class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        for idx, c in enumerate(s[::-1]):
            if c == ' ' and count > 0:
                break
            if c != ' ':
                count += 1
        
        return count

if __name__ == "__main__":
    print Solution().lengthOfLastWord('Hello World')
    print Solution().lengthOfLastWord('HelloWorld')
    print Solution().lengthOfLastWord('abc ')
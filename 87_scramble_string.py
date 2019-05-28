class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.dict = {}
        def f(s1, s2):
            if len(s1) != len(s2) or sorted(s1) != sorted(s2): 
                return False
            if len(s1) < 4:
                return True

            if (s1, s2) in self.dict:
                return self.dict[(s1, s2)]

            for idx in xrange(1, len(s1)):
                if f(s1[:idx], s2[:idx]) and f(s1[idx:], s2[idx:]) or \
                   f(s1[:idx], s2[-idx:]) and f(s1[idx:], s2[:-idx]):
                   return True
        return f(s1, s2)
        
if __name__ == "__main__":
    print Solution().isScramble("great", "rgeat")

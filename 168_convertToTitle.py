class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        c_map = [ chr(i + ord('A')) for i in xrange(26)]
        ans = []
        
        while n > 0:
          n, r = divmod(n, 26)
          if r == 0: n -= 1
          ans.append(r-1)

        result = ''.join(map(lambda x: c_map[x], ans[::-1]))

        return result

if __name__ == "__main__":
    # print ord('A')
    # print chr(1)
    for value in xrange(1, 10):
      print Solution().convertToTitle(value)
    # print Solution().convertToTitle(26)
    # print Solution().convertToTitle(27)
    # print Solution().convertToTitle(53)
    # print Solution().convertToTitle(677)
    # print Solution().convertToTitle(27)
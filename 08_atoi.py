class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        result = ''
        for idx, s in enumerate(str):
          if idx == 0 and s in ['-', '+']:
            result += s
            continue  
          if not s.isdigit(): 
            break
          result += s

        try:
          return min(max( -(2 ** 31), int(result)), 2 ** 31 -1)
        except:
          return 0
if __name__ == "__main__":
    print Solution().myAtoi("")
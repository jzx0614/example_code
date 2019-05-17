class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for idx, c in enumerate(s[:-1]):
          num = roman_map[c]
          sum +=  (-num) if roman_map[s[idx+1]] > num else num
        sum += roman_map[s[-1]]
        return sum
if __name__ == "__main__":
    print Solution().romanToInt("LVIII")
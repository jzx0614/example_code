class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # units = ["", "I","II","III","IV","V","VI","VII","VIII","IX"]
        # tens = map(lambda x: x.replace("X","C").replace("V", "L").replace("I", "X"), units)
        # hundreds = map(lambda x: x.replace("X","M").replace("V", "D").replace("I", "C"), units)
        # thousands = ["", "M", "MM", "MMM"]

        # roman_map = [units, tens, hundreds, thousands]
        roman_map = [
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], 
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], 
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], 
            ['', 'M', 'MM', 'MMM']
        ]
        num_len = len(str(num))
        output_str = ""
        digital = 0
        while num != 0:
            output_str = roman_map[digital][num % 10] + output_str
            num /= 10
            digital += 1

        return output_str

if __name__ == "__main__":
    print Solution().intToRoman(1994)
        
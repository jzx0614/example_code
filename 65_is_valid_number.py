class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        useExponent = False
        userNumber = False
        usePoint = False
        afterExponent = True
        for idx, c in enumerate(s):
            if '0' <= c  <= '9':
                userNumber = True
                afterExponent = True
            elif c == 'e':
                if not userNumber or useExponent:
                    return False
                afterExponent = False
                useExponent = True
            elif c in ['+', '-']:
                if not (idx == 0 or s[idx-1] == 'e'):
                    return False
            elif c == '.':
                if (useExponent or usePoint):
                    return False
                usePoint = True
            else: 
                return False

        return userNumber and afterExponent

if __name__ == "__main__":
    print Solution().isNumber('2e0')
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = ''
        max_len = max(len(a), len(b))
        carry = 0
        for i in xrange(max_len):
            v1, v2 = 0, 0
            if a:
                v1 = int(a[-1])
                a = a[:-1]
            if b:
                v2 = int(b[-1])
                b = b[:-1]
            v = v1 + v2 + carry
            carry = v / 2
            output = str(v%2) + output
            
        if carry == 1:
            output = '1' + output
        return output
        
if __name__ == "__main__":
    print Solution().addBinary("1010", "1011")
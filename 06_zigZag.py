class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        period = 2 * (numRows - 1)
        lines = ["" for i in range(numRows)]
        d = {}  # dict remainder:line
        for i in xrange(period):
            if i < numRows:
                d[i] = i
            else:
                d[i] = period - i
        print d
        for i in xrange(len(s)):
            lines[d[i % period]] += s[i]
        print lines
        return "".join(lines)

if __name__ == "__main__":
    s = "123456789ABCDE"
    numRows = 5
    print Solution().convert(s, numRows)

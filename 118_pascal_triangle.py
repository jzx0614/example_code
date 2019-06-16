class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        pascal = [1, 1]
        for row in xrange(2, rowIndex+1):
            new_list = pascal[:]
            for idx in xrange(1,  row):
                new_list[idx] = pascal[idx] + pascal[idx-1]
            new_list.append(1)
            pascal = new_list
        return pascal

if __name__ == "__main__":
    print Solution().getRow(2)
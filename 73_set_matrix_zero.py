class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = set() 
        col = set()

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in row:
            for j in xrange(len(matrix[0])):
                matrix[i][j] = 0
        for j in col:
            for i in xrange(len(matrix)):
                matrix[i][j] = 0

        print matrix    
if __name__ == "__main__":
    Solution().setZeroes([
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ])
    
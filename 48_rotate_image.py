class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def print_matrix():
            for row in matrix:
                print row
            print

        last = len(matrix) - 1
        for x in xrange(len(matrix)):
            for y in xrange(x, last-x):
                matrix[x][y], matrix[y][last-x], matrix[last-x][last-y], matrix[last-y][x] = \
                     matrix[last-y][x], matrix[x][y], matrix[y][last-x], matrix[last-x][last-y]
        print_matrix()

if __name__ == "__main__":
    Solution().rotate([[0]])
    Solution().rotate([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]])
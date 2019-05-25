class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row_index, start, end = 0, 0, len(matrix) - 1
        
        while start <= end:
            mid = (start + end) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                row_index = mid
                start = mid + 1
            else:
                end = mid - 1

        start, end = 0, len(matrix[row_index]) -1 
        while start <= end:
            mid = (start + end) / 2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False

if __name__ == "__main__":
    # Solution().searchMatrix([
    #     [1,   3,  5,  7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ], 0)
    print  Solution().searchMatrix([[2, 3, 5]], 1)
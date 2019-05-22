class Solution(object):
    # def spiralOrder(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     if len(matrix) == 0:
    #         return []
    #     max_row = len(matrix) - 1
    #     max_col = len(matrix[0]) - 1
    #     total_len = len(matrix) * len(matrix[0])
    #     output = []
    #     direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    #     d_idx = 0
    #     x, y = 0, -1
    #     while len(output) < total_len:
    #         pre_x, pre_y = x, y
    #         x, y = x + direct[d_idx][0], y + direct[d_idx][1]
    #         if not(0 <= x <= max_row and 0 <= y <= max_col) or matrix[x][y] == '-':
    #             d_idx = (d_idx + 1) % 4
    #             x, y = pre_x + direct[d_idx][0], pre_y + direct[d_idx][1]
    #         output.append(matrix[x][y])
    #         matrix[x][y] = '-'
    #     return output

    def spiralOrder(self, matrix):
        result = []
        
        while matrix and matrix[0]:
            if matrix[0]:
                result += matrix.pop(0)
            
            if matrix and matrix[0]:
                result += [row.pop() for row in matrix]
            
            if matrix and matrix[-1]:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                result += [ row.pop(0) for row in matrix[::-1]]
        
        return result

if __name__ == "__main__":
    print Solution().spiralOrder([
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ])
    # print Solution().spiralOrder([
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9,10,11,12]
    # ])
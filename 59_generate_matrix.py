class Solution(object):
    def generateMatrix(self, n):
        if n == 0: return []

        matrix = [[0] * n for _ in xrange(n)]

        total_len = n * n
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        idx = d_idx = 0
        x, y = 0, -1
        while idx < total_len:
            pre_x, pre_y = x, y
            x, y = x + direct[d_idx][0], y + direct[d_idx][1]

            if not(0 <= x < n and 0 <= y < n) or matrix[x][y] != 0:
                d_idx = (d_idx + 1) % 4
                x, y = pre_x + direct[d_idx][0], pre_y + direct[d_idx][1]
            matrix[x][y] = idx + 1
            idx += 1
            
        return matrix

if __name__ == "__main__":
    print Solution().generateMatrix(4)
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1: return 1 if grid[0][0] == 0 else -1 
        start, end = (0, 0), (n-1, n-1)
        if (grid[0][0] == 1 or grid[-1][-1] == 1): return -1
        direction = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

        queue = deque([(0, 0, 1)])
        while queue:
            pos_x, pos_y, length = queue.popleft()
            for x, y in ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)):
                new_pos_x, new_pos_y = (pos_x + x, pos_y + y)
                if not (0 <= new_pos_x < n and 0 <= new_pos_y < n) or grid[new_pos_x][new_pos_y] != 0: continue

                if new_pos_x == end[0] and new_pos_y == end[1]:
                    return length + 1
                grid[new_pos_x][new_pos_y] = 2
                queue.append((new_pos_x, new_pos_y, length + 1))
        return -1 




if __name__ == "__main__":
    print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
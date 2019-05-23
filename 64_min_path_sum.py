class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        for i in xrange(m):
            for j in xrange(n):
                if i == j == 0: continue
                left = 1e9 if j == 0 else grid[i][j-1]
                up = 1e9 if i == 0 else grid[i-1][j]
                grid[i][j] += min(left, up)

                print grid

        print grid
        return grid[-1][-1]

if __name__ == "__main__":
    print Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])        
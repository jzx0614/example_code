class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid: return 1
        obstacleGrid[0][0] = obstacleGrid[0][0] ^ 1
        for idx in xrange(1, len(obstacleGrid[0])):
            obstacleGrid[0][idx] = 0 if obstacleGrid[0][idx] == 1 else obstacleGrid[0][idx-1]

        for idx in xrange(1, len(obstacleGrid)):
            obstacleGrid[idx][0] = 0 if obstacleGrid[idx][0] == 1 else obstacleGrid[idx-1][0]

        for x in xrange(1, len(obstacleGrid)):
            for y in xrange(1, len(obstacleGrid[0])):
                obstacleGrid[x][y] = 0 if obstacleGrid[x][y] == 1 else obstacleGrid[x-1][y] + obstacleGrid[x][y-1]
        
        return obstacleGrid[-1][-1]

if __name__ == "__main__":
    print Solution().uniquePathsWithObstacles([
  [1]
])

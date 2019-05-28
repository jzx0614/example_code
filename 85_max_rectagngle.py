class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 : return 0

        max_value = 0
        height = len(matrix[0]) * [0]
        for row in matrix:
            for idx, col in enumerate(row):
                if col == '1':
                    height[idx] += 1
                else:
                    height[idx] = 0
            value = self.max_rectangle(height[:])
            print row, value, height
            max_value = max(max_value, value)
        return max_value
    
    def max_rectangle(self, height):
        height.append(0)
        stack = [-1]
        max_value = 0
        for idx, value in enumerate(height):
            while stack and value < height[stack[-1]]:
                h = height[stack.pop()]
                w = idx - stack[-1] - 1
                max_value = max(max_value, w*h)
            stack.append(idx)
        return max_value

if __name__ == "__main__":
    print Solution().maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])